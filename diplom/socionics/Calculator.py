from diplom.socionics import Relation
from diplom.socionics import Psychotype


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
        psychos = []
        for i, num in zip(range(1, 17), collective):
            if num == 0:
                continue
            for _ in range(num):
                psychos.append(Psychotype(i, None))
        res = [[0]*len(psychos) for _ in psychos]
        for i, psycho in enumerate(psychos):
            for j, other in enumerate(psychos):
                res[i][j] = grades[self[psycho, other].relation-1]
        return res

