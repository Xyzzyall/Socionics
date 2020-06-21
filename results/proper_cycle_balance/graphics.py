from diplom.analyzer import Visualizer
from matplotlib import pyplot as plt
from diplom.socionics.Calculator import Calculator


class BalanceStats(Visualizer):
    fig = plt.Figure
    axs = plt.Axes

    def __init__(self):
        Visualizer.__init__(self, 'results.sqlite')

    def show_balance_stat(self, res_id: int):
        self.plot_balance_stat(res_id, self.axs, field_name='balance', label='Баланс без учета длины циклов')

    def show_weight_balance_stat(self, res_id: int):
        self.plot_balance_stat(res_id, self.axs, field_name='balance_len', label='Баланс с учетом длины циклов')

    def show_both_balance_stat(self, res_id: int, socio_filter=None):
        self.plot_balance_stat(res_id, self.axs, socio_filter=socio_filter, field_name='balance', label='Баланс без учета длины циклов', hist_shift=-.5/Visualizer.STAT_DOTS)
        self.plot_balance_stat(res_id, self.axs, socio_filter=socio_filter, field_name='balance_len', label='Баланс с учетом длины циклов', hist_shift=.5/Visualizer.STAT_DOTS)

    def run(self) -> None:
        Visualizer.run(self)

        res_id = int(input('result id = '))
        stats = {'all', 'quadras'}
        what_stats = input(f'what stat? (one from {str(stats)}): ')
        assert what_stats in stats

        if what_stats == 'all':
            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            self.show_balance_stat(res_id)
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Мера баланса без учета длины циклов')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            self.show_weight_balance_stat(res_id)
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Мера баланса c учетом длины циклов')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            self.show_both_balance_stat(res_id)
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Совмещенная гистограмма')
            self.axs.legend()
            plt.show()
            print('fin!')
        elif what_stats == 'quadras':
            def quadras_filter(group, quadras):
                q = Calculator.get_quadras_in_group(group)
                for quadra, filt in zip(q, quadras):
                    if quadra not in filt:
                        return False
                return True

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q0_2_0_2 = ((0,), (2,), (0,), (2,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q0_2_0_2))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (два человека из 2 квадры, два человека из 4 квадры)')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q2_0_2_0 = ((2,), (0,), (2,), (0,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q2_0_2_0))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (два человека из 1 квадры, два человека из 3 квадры)')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q2_0_0_2 = ((2,), (0,), (0,), (2,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q2_0_0_2))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (два человека из 1 квадры, два человека из 4 квадры)')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q2_0_0_2 = ((2,), (2,), (0,), (0,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q2_0_0_2))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (два человека из 1 квадры, два человека из 2 квадры)')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q4_0_0_0 = ((4,), (0,), (0,), (0,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q4_0_0_0))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (4 человека из 1 квадры)')
            self.axs.legend()
            plt.show()

            self.fig, self.axs = plt.subplots(1, 1, figsize=(16, 9))
            q1_1_1_1 = ((1,), (1,), (1,), (1,))
            self.show_both_balance_stat(res_id, lambda group: quadras_filter(group, q1_1_1_1))
            self.axs.set_ylabel('Групп с балансом X')
            self.axs.set_xlabel('Мера баланса b(G)')
            self.axs.set_title('Баланс групп (4 человека из разных квадр)')
            self.axs.legend()
            plt.show()


visuals = BalanceStats()
visuals.run()
visuals.db.close()