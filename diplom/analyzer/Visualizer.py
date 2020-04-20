from matplotlib import pyplot as plt
from diplom.database import DataBase
from diplom.database.DataBase import Request
import numpy as np


get_collectives_request = """
SELECT blocks, all_cycles, positive_cycles, negative_cycles FROM collective
"""


def draw_cycles_stat(db_file: str, blocks_cutoff: set = None):
    def normalize(arr: list, mn: int = None, mx: int = None):
        mn = mn if mn else min(arr)
        mx = mx if mx else max(arr)
        for i, val in enumerate(arr):
            arr[i] = (val - mn) / (mx - mn)

    db = DataBase.database_as_wrapper(db_file, 'kill me softly')

    data = []
    db.wrp_execute_request(Request(get_collectives_request, lambda d: data.append(d)))
    data = data[0]

    # getting stats
    pos_stats = list(range(31))
    neg_stats = list(range(31))
    all_stats = list(range(31))

    for d in data:
        blocks, all_cycles, pos_cycles, neg_cycles = d
        if blocks_cutoff:
            if blocks not in blocks_cutoff:
                continue
        if all_cycles < len(pos_stats) - 1:
            pos_stats[all_cycles] += pos_cycles
            neg_stats[all_cycles] += neg_cycles
            all_stats[all_cycles] += 1

    # normalizing
    normalize(all_stats)
    mx = max(max(pos_stats), max(neg_stats))
    mn = min(min(pos_stats), min(neg_stats))
    normalize(pos_stats, mn, mx)
    normalize(neg_stats, mn, mx)


    fig, axs = plt.subplots(1, 1, figsize=(9, 3))
    line1 = axs.plot(range(31), pos_stats, label='Положительные циклы')
    line2 = axs.plot(range(31), neg_stats, label='Отрицательные циклы')
    line3 = axs.plot(range(31), all_stats, label='Кол-во групп с таким количеством циклов', dashes=[6, 2])

    axs.set_ylabel('Относительное количество (норм. min max)')
    axs.set_title('Связь кол-ва полож. и отриц. циклов к кол-ву всех циклов.')

    axs.legend()
    plt.show()


def draw_balance_to_cycles(db_file: str):
    db = DataBase.database_as_wrapper(db_file, 'kill me softly')

    data = []
    db.wrp_execute_request(Request(get_collectives_request, lambda d: data.append(d)))
    data = data[0]

    pos_stats = list(range(5))
    neg_stats = list(range(5))
    all_stats = list(range(5))
    accounts_per_blocks = list(range(5))
    for d in data:
        blocks, all_cycles, pos_cycles, neg_cycles = d
        pos_stats[blocks] += pos_cycles
        neg_stats[blocks] += neg_cycles
        all_stats[blocks] += all_cycles
        accounts_per_blocks[blocks] += 1

    for blocks in range(5):
        pos_stats[blocks] /= accounts_per_blocks[blocks]
        neg_stats[blocks] /= accounts_per_blocks[blocks]
        all_stats[blocks] /= accounts_per_blocks[blocks]

    x = np.arange(5)
    width = 0.35
    fig, axs = plt.subplots(1, 1, figsize=(9, 3))
    rect1 = axs.bar(x - width / 3, pos_stats, width/3, label='Положительные циклы')
    rect2 = axs.bar(x, neg_stats, width/3, label='Отрицательные циклы')
    rect3 = axs.bar(x + width / 3, all_stats, width/3, label='Все циклы')

    axs.set_ylabel('Кол-во циклов/записей')
    axs.set_title('Статистика циклов в графах к блокам в сбалансированной матрице')
    axs.set_xticks(x)
    axs.legend()

    plt.show()
