from diplom.socionics import Relation


class Calculator:
    psycho_table = []

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
        return self.psycho_table[item[0].psycho][item[1].psycho]

