from matplotlib import pyplot as plt
from collections import defaultdict
import MySocioParser as parser


class MySocioStats:
    statistics = defaultdict(float)
    wrongs_stat = defaultdict(int)
    accounts = 0

    def __init__(self, file: str):
        f = open(file, 'r')
        for line in f:
            self.add_data(parser.MySocioData(line))
            self.accounts += 1
        f.close()
        #self.normalize()

    def add_data(self, data: parser.MySocioData):
        for typ in data.types:
            self.statistics[typ.name] += typ.percentage
        for wrong in data.wrongs:
            self.wrongs_stat[wrong] += 1

    def normalize(self):
        mx = max(self.wrongs_stat.values())
        mn = min(self.wrongs_stat.values())
        for key in self.wrongs_stat.keys():
            val = self.wrongs_stat[key]
            self.wrongs_stat[key] = (val - mn)/(mx - mn)

    def show_plot(self):
        fig, axs = plt.subplots(1, 2, figsize=(9, 3))
        axs[0].barh(range(16), self.statistics.values(), align='center')
        axs[0].set_yticks(range(16))
        axs[0].set_yticklabels(list(self.statistics.keys()))
        axs[0].invert_yaxis()
        axs[0].set_xlabel('Вероятностей')
        axs[0].set_title('Диаграмма распределения социотипов.')
        axs[1].bar(self.wrongs_stat.keys(), self.wrongs_stat.values())
        axs[1].set_title('Диаграмма "недостоверных" признаков.')
        fig.suptitle('Статистика сайта MySocio.ru\n' + str(self.accounts) + ' записей.')
        plt.show()

    def __str__(self):
        return 'There are ' + str(self.accounts) + ' accounts.\nTypes: ' +\
               str(self.statistics) + '\nWrongs: ' + str(self.wrongs_stat)
