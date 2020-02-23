from matplotlib import pyplot as plt
from collections import defaultdict
import MySocioParser as parser
import random


class MySocioStats:
    class Stats:
        statistics = defaultdict(float)
        wrongs_stat = defaultdict(int)
        accounts = 0

        def add_data(self, data: parser.MySocioData):
            for typ in data.types:
                self.statistics[typ.name] += typ.percentage
            for wrong in data.wrongs:
                self.wrongs_stat[wrong] += 1
            self.accounts += 1

        def normalize(self):
            for key in self.statistics.keys():
                self.statistics[key] /= self.accounts

            mx = max(self.wrongs_stat.values())
            mn = min(self.wrongs_stat.values())
            for key in self.wrongs_stat.keys():
                val = self.wrongs_stat[key]
                self.wrongs_stat[key] = (val - mn) / (mx - mn)

        def __str__(self):
            return 'There are ' + str(self.accounts) + ' accounts.\nTypes: ' + \
                   str(self.statistics) + '\nWrongs: ' + str(self.wrongs_stat)

    all_stats = None
    stats_random_300 = None
    stats_just_max_type = None

    def __init__(self, file: str):
        self.all_stats, self.stats_random_300, self.stats_just_max_type = MySocioStats.Stats(), MySocioStats.Stats(), MySocioStats.Stats()
        f = open(file, 'r')
        for line in f:
            data = parser.MySocioData(line)
            self.all_stats.add_data(data)
            data.types = [data.get_max_sociotype()]
            self.stats_just_max_type.add_data(data)

        self.all_stats.normalize()
        self.stats_just_max_type.normalize()
        f.close()
        f = open(file, 'r')
        for line in f:
            if random.randint(0, self.all_stats.accounts) <= 300:
                self.stats_random_300.add_data(parser.MySocioData(line))
        self.stats_random_300.normalize()
        f.close()

    def show_plot(self):
        def draw_stats(axis, stats):
            axis.barh(range(16), stats.statistics.values(), align='center')
            axis.set_yticks(range(16))
            axis.set_yticklabels(list(stats.statistics.keys()))
            axis.invert_yaxis()
            axis.set_xlabel('Вероятностей/записей')
            axis.set_title('Диаграмма распределения социотипов.')

        def draw_wrongs(axis, stats):
            axis.bar(stats.wrongs_stat.keys(), stats.wrongs_stat.values())
            axis.set_title('Диаграмма "недостоверных" признаков.')

        plt.figure(0)
        fig, axs = plt.subplots(1, 2, figsize=(9, 3))
        draw_stats(axs[0], self.all_stats)
        draw_wrongs(axs[1], self.all_stats)
        fig.suptitle('Статистика сайта MySocio.ru\n' + str(self.all_stats.accounts) + ' записей.')

        plt.figure(1)
        fig, axs = plt.subplots(1, 2, figsize=(9, 3))
        draw_stats(axs[0], self.stats_just_max_type)
        draw_stats(axs[1], self.all_stats)
        axs[1].set_title('Диаграмма с учетом всех вероятностей.')
        fig.suptitle('Статистика наиболее вероятных типов\n' + str(self.stats_just_max_type.accounts) + ' записей.')

        plt.figure(2)
        fig, axs = plt.subplots(2, 2, figsize=(9, 3))
        draw_stats(axs[0][0], self.stats_random_300)
        draw_wrongs(axs[0][1], self.stats_random_300)
        draw_stats(axs[1][0], self.all_stats)
        draw_wrongs(axs[1][1], self.all_stats)
        fig.suptitle('~300 cлучайных записей.\n' + str(self.stats_random_300.accounts) + ' записей.')

        plt.show()


    def __str__(self):
        return 'All: ' + str(self.all_stats) + '\nRandom ~200: '

