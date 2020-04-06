from old import Sociometrica as SM, BinRelAnalysis as BA
import itertools
import time
from threading import Thread


class Daemon(Thread):
    threads_in_work = 0
    threads = 0
    collect = 0

    def __init__(self, threads: int, collect: int):
        Thread.__init__(self)
        self.threads = threads
        self.collect = collect

    def thread_generator(self):
        for p in itertools.product([1, 0, -1], repeat=7):
            grades = SM.Grades({
                'TO': 1, 'DU': 1, 'AK': 1, 'ZE': 1,
                'R-': -1, 'Z-': -1, 'MI': p[0], 'DE': p[6],
                'SE': p[1], 'PO': p[2], 'KT': p[3], 'KF': -1,
                'R+': -1, 'Z+': -1, 'PD': p[4], 'RO': p[5]
            })
            yield GradeAnalysisThread(grades, self.collect, self)

    def thread_started(self):
        self.threads_in_work += 1

    def thread_finished(self):
        self.threads_in_work -= 1

    def run(self):
        g = self.thread_generator()
        try:
            while True:
                if self.threads_in_work < self.threads:
                    next(g).start()
                time.sleep(0.001)
        except StopIteration:
            print('finished')


class GradeAnalysisThread(Thread):
    grade = None
    ca = None
    daemon = None

    def __init__(self, grade: SM.Grades, collect: int, daemon: Daemon):
        Thread.__init__(self)
        self.grade = grade
        self.daemon = daemon
        self.ca = BA.Analysis(BA.Collective(collect), self.grade, 'TestData/res.txt')

    def run(self):
        self.daemon.thread_started()
        self.ca.analyze()
        self.daemon.thread_finished()


d = Daemon(6, 4)
d.run()

