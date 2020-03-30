from old import MySocioParser

max_ind = 4009200

indexes = list(range(3500000, max_ind, 100))

f = open('my_socio_data.txt', 'a')

i = 0
for data in MySocioParser.mysocio_crawler(indexes, sleep=0.3):
    try:
        i += 1
        if i % 10 == 0:
            print('loaded ' + str(i) + ' results.')
        f.write('\n' + data)
    except:
        f.close()
        break

f.close()
