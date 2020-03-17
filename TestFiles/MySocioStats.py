import MySocioParser as parser

stats = parser.MySocioStats('TestData/my_socio_data.txt')
print(stats)

stats.show_plot()