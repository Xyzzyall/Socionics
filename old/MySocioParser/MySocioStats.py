from matplotlib import pyplot as plt
from collections import defaultdict
from old import MySocioParser as parser, Socionics as soc
import random


class MySocioStats:
    class SimpleStats:
        statistics = defaultdict(float)
        wrongs_stat = defaultdict(int)
        accounts = 0

        def __init__(self):
            self.statistics = defaultdict(float)
            self.wrongs_stat = defaultdict(int)
            self.accounts = 0

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

    class RelationsStats:
        statistics = defaultdict(float)
        __num__ = 0

        def add_data(self, data: parser.MySocioData):
            typ = old.MySocioParser.Utils.get_my_sociotype(data)
            #for name in soc.Psychotype.get_names():
            #    self.add_to_stat(soc.Psychotype.get(name).mult(typ))
            self.add_to_stat(soc.Psychotype.get('Gs').mult(typ))
            self.__num__ += 1

        def add_to_stat(self, relation: soc.Relation):
            decomposed = soc.decompose(soc.Relation, relation)
            for key in decomposed.keys():
                self.statistics[key] += decomposed[key]

        def normalize(self):
            """"""
            """mx = max(self.statistics.values())
            mn = min(self.statistics.values())
            for key in self.statistics.keys():
                val = self.statistics[key]
                self.statistics[key] = (val - mn) / (mx - mn)"""
            mx = max(self.statistics.values())
            for key in self.statistics.keys():
                val = self.statistics[key]
                self.statistics[key] = val / mx

        def __str__(self):
            return str(self.statistics)

    class AccuracyStat:
        statistics = {name: [float(), int()] for name in soc.Psychotype.get_names()}

        def add_data(self, data: parser.MySocioData):
            for typ in data.types:
                val = self.statistics[old.MySocioParser.Utils.mysocio_type_convert(typ.name)]
                val[0] += typ.percentage
                val[1] += 1

        def normalize(self):
            for key in self.statistics.keys():
                val = self.statistics[key]
                val[0] = val[0]/val[1] * 100.0

        def get_values(self):
            return [val[0] for val in self.statistics.values()]

    all_stats = None
    stats_random_300 = None
    stats_just_max_type = None
    stats_relations = None
    stats_accuracy = None

    def __init__(self, file: str):
        self.all_stats = MySocioStats.SimpleStats()
        self.stats_random_300 = MySocioStats.SimpleStats()
        self.stats_just_max_type = MySocioStats.SimpleStats()
        self.stats_relations = MySocioStats.RelationsStats()
        self.stats_accuracy = MySocioStats.AccuracyStat()
        f = open(file, 'r')
        for line in f:
            data = parser.MySocioData(line)
            self.all_stats.add_data(data)
            data.types = [data.get_max_sociotype()]
            self.stats_just_max_type.add_data(data)
            #self.stats_relations.add_data(data)
            self.stats_accuracy.add_data(data)
        self.stats_accuracy.normalize()
        self.all_stats.normalize()
        self.stats_just_max_type.normalize()
        f.close()

        f = open(file, 'r')
        for line in f:
            if random.randint(0, self.all_stats.accounts) <= 300:
                data = parser.MySocioData(line)
                self.stats_random_300.add_data(data)

        self.stats_random_300.normalize()
        #self.stats_relations.normalize()
        f.close()

    def show_plot(self):
        def rename_types(stats: dict):
            new = {}
            for key in old.MySocioParser.Utils.psycho_map.keys():
                new[old.MySocioParser.Utils.psycho_map[key]] = stats[key.capitalize()]
            return new

        def draw_stats(axis, stats):
            ln = len(stats.statistics.keys())
            axis.barh(range(ln), stats.statistics.values(), align='center')
            axis.set_yticks(range(ln))
            axis.set_yticklabels(list(stats.statistics.keys()))
            axis.invert_yaxis()
            axis.set_xlabel('Вероятностей/записей')
            axis.set_title('Диаграмма распределения социотипов.')

        def draw_wrongs(axis, stats):
            axis.bar(stats.wrongs_stat.keys(), stats.wrongs_stat.values())
            axis.set_title('Диаграмма "недостоверных" признаков.')

        self.all_stats.statistics = rename_types(self.all_stats.statistics)
        self.stats_just_max_type.statistics = rename_types(self.stats_just_max_type.statistics)
        self.stats_random_300.statistics = rename_types(self.stats_random_300.statistics)
        #self.stats_accuracy.statistics = rename_types(self.stats_accuracy.statistics)

        plt.figure(0)
        fig, axs = plt.subplots(1, 2, figsize=(9, 3))
        draw_stats(axs[0], self.all_stats)
        draw_wrongs(axs[1], self.all_stats)
        fig.suptitle('Статистика сайта MySocio.ru\n' + str(self.all_stats.accounts) + ' записей.')

        plt.figure(1)
        fig, axs = plt.subplots(2, 1, figsize=(9, 3))
        draw_stats(axs[0], self.stats_just_max_type)
        draw_stats(axs[1], self.all_stats)
        axs[1].set_title('Диаграмма с учетом всех вероятностей.')
        fig.suptitle('Статистика наиболее вероятных типов\n' + str(self.stats_just_max_type.accounts) + ' записей.')

        plt.figure(2)
        fig, axs = plt.subplots(2, 1, figsize=(9, 3), sharex=True)
        draw_stats(axs[0], self.stats_random_300)
        #draw_wrongs(axs[0][1], self.stats_random_300)
        draw_stats(axs[1], self.all_stats)
        #draw_wrongs(axs[1][1], self.all_stats)
        fig.suptitle('~300 cлучайных записей.\n' + str(self.stats_random_300.accounts) + ' записей.')

        plt.figure(3)
        fig, axs = plt.subplots(1, 1, figsize=(9, 3))
        axs.bar(self.stats_accuracy.statistics.keys(), self.stats_accuracy.get_values())
        axs.set_title('Диаграмма точности определения признаков.')

        plt.figure(4)
        fig, axs = plt.subplots(1, 1, figsize=(9, 3))
        draw_stats(axs, self.stats_relations)
        axs.set_title('Диаграмма распределения отношений.')
        axs.set_xlabel('Вероятностей')
        fig.suptitle('Отношения.')

        diff_stats = MySocioStats.SimpleStats()
        diff_stats.statistics = {key: self.all_stats.statistics[key] - self.stats_just_max_type.statistics[key] for key in self.all_stats.statistics}
        mx = max(diff_stats.statistics.values())
        mn = min(diff_stats.statistics.values())
        for key in diff_stats.statistics:
            val = diff_stats.statistics[key]
            diff_stats.statistics[key] = (val - mn) / (mx - mn)
        plt.figure(5)
        fig, axs = plt.subplots(1, 1, figsize=(9, 3))
        draw_stats(axs, diff_stats)
        fig.suptitle('Разница наиболее вероятных типов и всех типов.\n' + str(self.stats_just_max_type.accounts) + ' записей.')

        random_diff = MySocioStats.SimpleStats()
        random_diff.statistics = {key: abs(self.stats_random_300.statistics[key] - self.all_stats.statistics[key]) for key
                                 in self.all_stats.statistics}
        random_diff.statistics['min'] = min(list(self.all_stats.statistics.values()))
        plt.figure(6)
        fig, axs = plt.subplots(1, 1, figsize=(9, 3))
        draw_stats(axs, random_diff)
        fig.suptitle('Разница 300 и общей статистики.\n' + str(self.stats_just_max_type.accounts) + ' записей.')

        plt.show()

    def __str__(self):
        return 'All: ' + str(self.all_stats) + '\nRandom ~300: ' + str(self.stats_random_300)
