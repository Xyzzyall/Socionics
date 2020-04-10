from threading import Thread

from diplom.analyzer import Analyzer
from diplom.analyzer import AnalyzerTask
from diplom.database import DataBase
from itertools import product

database_tables = """
CREATE TABLE grade(
    rowid INTEGER PRIMARY KEY,
    ps_TO INTEGER,
    ps_DU INTEGER,
    ps_AK INTEGER,
    ps_ZE INTEGER,
    ps_R_min INTEGER,
    ps_Z_min INTEGER,
    ps_MI INTEGER,
    ps_DE INTEGER,
    ps_SE INTEGER,
    ps_PO INTEGER,
    ps_KT INTEGER,
    ps_KF INTEGER,
    ps_R_plus INTEGER,
    ps_Z_plus INTEGER,
    ps_PD INTEGER,
    ps_RO INTEGER
);
CREATE TABLE grade_stats(
    rowid INTEGER PRIMARY KEY,
    grade_id INTEGER,
    group_size INTEGER,
    balanced0 INTEGER,
    balanced1 INTEGER,
    balanced2 INTEGER,
    balanced3 INTEGER,
    balanced_other INTEGER,
    FOREIGN KEY(grade_id) REFERENCES grade(rowid)
);
CREATE TABLE collective(
    rowid INTEGER PRIMARY KEY,
    grade_stats_id INTEGER,
    name TEXT,
    blocks INTEGER,
    perms TEXT,
    FOREIGN KEY(grade_stats_id) REFERENCES grade_stats(rowid)
)
"""


def run_db():
    db = DataBase('results/balance_results/results.sqlite', database_tables)
    db.start()
    return db


class Analysis(Thread):
    db = DataBase

    def __init__(self, db: DataBase):
        Thread.__init__(self, name='analysis')
        self.db = db

    def run(self) -> None:
        def grades_generator():
            for grade in product([1, 0, -1], repeat=5):
                yield (1, 1, 1, 1, -1, 1, 1, grade[0], -1, grade[1], grade[2], grade[3], -1, -1, grade[4], -1)

        collective_size = 4

        for i, grade in enumerate(grades_generator()):
            task = AnalyzerTask(collective_size, grade)
            analyzer = Analyzer(task, f'num{i}', self.db)
            analyzer.start()
            analyzer.join()


db = run_db()
analysis = Analysis(db)
analysis.start()
analysis.join()
