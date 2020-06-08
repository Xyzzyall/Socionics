from diplom.socionics import Relation
from diplom.socionics import Psychotype
import networkx as netx
from collections import defaultdict

class Calculator:
    psycho_table = list

    def __init__(self):
        # простите...
        self.psycho_table = [
            [Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), ],
            [Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), ],
            [Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), ],
            [Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), ],
            [Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), ],
            [Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), ],
            [Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), ],
            [Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), ],
            [Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), ],
            [Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), ],
            [Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), ],
            [Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), ],
            [Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), ],
            [Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), ],
            [Relation.get_by_name("PD"), Relation.get_by_name("RO"), Relation.get_by_name("R-"), Relation.get_by_name("Z-"), Relation.get_by_name("KT"), Relation.get_by_name("KF"), Relation.get_by_name("SE"), Relation.get_by_name("PO"), Relation.get_by_name("MI"), Relation.get_by_name("DE"), Relation.get_by_name("R+"), Relation.get_by_name("Z+"), Relation.get_by_name("AK"), Relation.get_by_name("ZE"), Relation.get_by_name("TO"), Relation.get_by_name("DU"), ],
            [Relation.get_by_name("RO"), Relation.get_by_name("PD"), Relation.get_by_name("Z-"), Relation.get_by_name("R-"), Relation.get_by_name("KF"), Relation.get_by_name("KT"), Relation.get_by_name("PO"), Relation.get_by_name("SE"), Relation.get_by_name("DE"), Relation.get_by_name("MI"), Relation.get_by_name("Z+"), Relation.get_by_name("R+"), Relation.get_by_name("ZE"), Relation.get_by_name("AK"), Relation.get_by_name("DU"), Relation.get_by_name("TO"), ],
        ]

    def __getitem__(self, item: tuple) -> Relation:
        return self.psycho_table[item[0].psycho-1][item[1].psycho-1]

    def get_collective(self, collective: tuple, grades: tuple):
        psychos = Calculator.get_psychotypes_from_vector(collective)
        res = [[0]*len(psychos) for _ in psychos]
        for i, psycho in enumerate(psychos):
            for j, other in enumerate(psychos):
                res[i][j] = grades[self[psycho, other].relation-1]
        return res

    @staticmethod
    def get_quadras_in_group(group: tuple) -> tuple:
        quadras = [0, 0, 0, 0]
        for typ, num in enumerate(group):
            if typ in range(0, 4):
                quadras[0] += num
            elif typ in range(4, 8):
                quadras[1] += num
            elif typ in range(8, 12):
                quadras[2] += num
            else:
                quadras[3] += num
        return tuple(quadras)

    @staticmethod
    def get_psychotypes_from_vector(vector: tuple):
        psychos = []
        for i, num in zip(range(1, 17), vector):
            if num == 0:
                continue
            for _ in range(num):
                psychos.append(Psychotype(i))
        return psychos

    @staticmethod
    def matrix_to_graph(m_graph: list, changes: dict = None, diag_to_null: bool = True):
        matrix = m_graph.copy()
        if diag_to_null:
            for x in range(len(matrix)):
                matrix[x][x] = 0

        connections = []
        res = netx.DiGraph()
        for x, row in enumerate(matrix):
            for y, edge in enumerate(row):
                if changes:
                    edge_changed = changes[edge]
                    if edge_changed == 1:
                        connections.append((x, y))
                else:
                    if edge:
                        connections.append((x, y, edge))

            if changes:
                res.add_edges_from(connections)
            else:
                res.add_weighted_edges_from(connections)

        return res

    @staticmethod
    def cycles_in_signed_graph(graph: netx.DiGraph):
        for cycle in netx.simple_cycles(graph):
            if len(cycle) < 3:
                continue
            sign = 1
            for edge0, edge1 in ((cycle[j-1], cycle[j]) for j in range(1, len(cycle))):
                sign *= graph[edge0][edge1]['weight']
            sign *= graph[cycle[-1]][cycle[0]]['weight']
            yield sign, cycle

    @staticmethod
    def count_cycles_in_signed_graph(graph: netx.DiGraph):
        pos_cycles = defaultdict(int)
        neg_cycles = defaultdict(int)
        pos_cycles[3] = 0
        neg_cycles[3] = 0

        for sign, cycle in Calculator.cycles_in_signed_graph(graph):
            if sign > 0:
                pos_cycles[len(cycle)] += 1
            else:
                neg_cycles[len(cycle)] += 1
        return pos_cycles, neg_cycles

    @staticmethod
    def balance(graph: netx.DiGraph):
        pos_cycles, neg_cycles = Calculator.count_cycles_in_signed_graph(graph)
        num_of_pos_cycles, num_of_neg_cycles = sum(pos_cycles.values()), sum(neg_cycles.values())
        num_of_cycles = num_of_pos_cycles + num_of_neg_cycles
        if num_of_cycles == 0:
            return 0.0
        else:
            return num_of_pos_cycles / num_of_cycles

    @staticmethod
    def balance_length_weighted(graph: netx.DiGraph):
        pos_cycles, neg_cycles = Calculator.count_cycles_in_signed_graph(graph)
        n = max(max(pos_cycles.keys()), max(neg_cycles.keys()))     # finding length of the longest cycle
        a, b = 0, 0  # b_l(G) = a / b
        for i in range(3, n+1):
            num_of_cycles = pos_cycles[i] + neg_cycles[i]
            a += pos_cycles[i] / i
            b += num_of_cycles / i

        if b == 0:
            return 0.0
        else:
            return a / b
