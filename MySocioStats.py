import MySocioParser as parser

stats = parser.MySocioStats('my_socio_data.txt')
print(stats)

stats.show_plot()