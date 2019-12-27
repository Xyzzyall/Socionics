import BinRelAnalysis as BA


class Analysis:
    collective = None
    grades = None
    output_file = ''

    def __init__(self, collective, grades, output_file):
        self.collective = collective
        self.grades = grades
        self.output_file = output_file

    def analyze(self):
        iterations = 0
        out = open(self.output_file, 'w')
        out.write("{'collective': " + str(self.collective.size) + ", 'grades': " + str(self.grades) + "}")
        grade_i = 0
        for grade in self.grades:
            res = '(' + str(grade_i) + ', {'
            coll_an = BA.CollectiveAnalysis(self.collective, grade)
            balanced_1b = 0
            balanced_2b = 0
            balanced_3b = 0
            non_balanced = 0
            for an_res in coll_an:
                if an_res[1][0]:
                    n = len(an_res[1][1])
                    if n == 1:
                        balanced_1b += 1
                    elif n == 2:
                        balanced_2b += 1
                    elif n == 3:
                        balanced_3b += 1
                    else:
                        non_balanced += 1
                else:
                    non_balanced += 1
                iterations += 1
                if iterations % 100 == 0:
                    print(str(iterations) + ' is done.')
            balanced = balanced_1b + balanced_2b
            res += "'balanced:'" + str(balanced) + ", '1 block:'" + str(balanced_1b) + ", '2 blocks:'" + \
                   str(balanced_2b) + ", '3 blocks:'" + str(balanced_3b) + ", 'non balanced:'" + str(non_balanced) + "}"
            out.write(res)
            grade_i += 1
            print('Grade ' + str(grade_i) + ' analyzed.')
        out.close()
        print('Analysis is done. Performed ' + str(iterations) + ' iterations, analyzed ' + str(grade_i+1) + ' grades.')