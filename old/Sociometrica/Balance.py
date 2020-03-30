import numpy as np


def balance(matrix: np.ndarray, u=True):
    n = len(matrix)
    d = matrix.copy()
    if u:
        for i in range(n):
            d[i, i] = 1

    def pred_sum(matrix, predicate):
        res = []
        for row in matrix:
            num = 0
            for elem in row:
                if predicate(elem):
                    num += elem
            res.append(num)
        return np.array(res).transpose()

    def is_subset(x: list, y: list):
        return set(y).issubset(set(x))

    def find_max(array):
        ind = 0
        mx = 0
        for i in range(len(array)):
            if array[i] > mx:
                mx = array[i]
                ind = i
        return ind

    def delete_rows(matrix, rows):
        res = []
        for i in range(len(matrix)):
            if not rows[i]:
                res.append(matrix[i])
        return np.array(res)

    a = d.copy()
    res = []
    n = np.array(list(range(n))).transpose()
    while len(a) > 0:
        s_list = pred_sum(a, lambda x: x > 0)
        i_star = find_max(s_list)
        pos_i_star_row = np.array([(1 if elem > 0 else 0) for elem in a[i_star]])
        s1 = np.matmul(a, pos_i_star_row.transpose())
        b = np.array([(1 if s1[i] == s_list[i] else 0) for i in range(len(s1))])
        #n1 = np.array([n, b])
        a = delete_rows(a, b)
        for i in range(len(b)):
            if b[i]:
                res.append(n[i])
        n = delete_rows(n, b)
    return res


def check_blocks(mat: np.ndarray):
    matrix = mat.copy()
    clasters = [[]]

    def compare_all(matrix, pred):
        for row in matrix:
            for elem in row:
                if not pred(elem):
                    return False
        return True

    def clear_block(mat, block):
        for i in block:
            for j in block:
                mat[i, j] = 0
        return mat

    pointer = 0
    claster = 0
    pred = lambda x: x >= 0
    for i in range(len(matrix)):
        if compare_all(matrix[pointer:i+1, pointer:i+1], pred):
            clasters[claster].append(i)
        else:
            matrix = clear_block(matrix, clasters[claster])
            clasters.append([i])
            claster += 1
            pointer = i
    matrix = clear_block(matrix, clasters[claster])
    blocked = compare_all(matrix, lambda x: x <= 0)
    return blocked, clasters
