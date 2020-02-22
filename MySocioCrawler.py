import MySocioParser
import random

max_ind = 4009200

indexes = list(range(7, max_ind, 1000))

f = open('my_socio_data.txt', 'w+')

i = 0
for data in MySocioParser.mysocio_crawler(indexes, sleep=0.1):
    i += 1
    if i%10 == 0:
        print('loaded ' + str(i) + ' results.')
    f.write(data + '\n')

f.close()
