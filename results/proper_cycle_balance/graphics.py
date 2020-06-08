from diplom.analyzer import Visualizer
from matplotlib import pyplot as plt


class BalanceStats(Visualizer):
    fig = plt.Figure
    axs = plt.Axes

    def __init__(self):
        Visualizer.__init__(self, 'results.sqlite')

    def show_balance_stat(self, res_id: int):
        self.plot_balance_stat(res_id, self.axs, field_name='balance', label='Баланс без учета длины циклов')

    def show_weight_balance_stat(self, res_id: int):
        self.plot_balance_stat(res_id, self.axs, field_name='balance_len', label='Баланс с учетом длины циклов')

    def show_both_balance_stat(self, res_id: int):
        self.plot_balance_stat(res_id, self.axs, field_name='balance', label='Баланс без учета длины циклов')
        self.plot_balance_stat(res_id, self.axs, field_name='balance_len', label='Баланс с учетом длины циклов', dashes=[3, 2])

    def run(self) -> None:
        Visualizer.run(self)

        self.fig, self.axs = plt.subplots(1, 1, figsize=(9, 3))
        res_id = int(input('result id = '))

        self.show_balance_stat(res_id)
        plt.show()
        input('next?')

        self.fig, self.axs = plt.subplots(1, 1, figsize=(9, 3))
        self.show_weight_balance_stat(res_id)
        plt.show()
        input('next?')

        self.fig, self.axs = plt.subplots(1, 1, figsize=(9, 3))
        self.show_both_balance_stat(res_id)
        plt.show()
        print('fin!')

visuals = BalanceStats()
visuals.run()
