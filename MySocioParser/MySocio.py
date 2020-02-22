from bs4 import BeautifulSoup
import requests
import re
import time


def parse_page(html):
    def format_soctype_name(src_tag):
        return re.findall(r'\((.*?)\)', src_tag.text)[0]

    def format_wrongs(src_tag):
        return re.findall(r'\w+', src_tag.text)[0]

    soup = BeautifulSoup(html, "html5lib")

    types = None
    wrongs = None

    for tag in soup.find_all('aside'):
        typ = tag.find('div', attrs={'class': 'ttl'}).text
        if typ == "Вероятные типы":
            types = [(format_soctype_name(typ_tags.find('div', attrs={'class': 'type-sign'})),
                      typ_tags.find('span', attrs={'class': 'type-percent'}).text)
                     for typ_tags in tag.find_all('div', attrs={'class': 'half'})]
        elif typ == "Недостоверные признаки":
            wrongs = [format_wrongs(wr_tags) for wr_tags in tag.find_all('div', attrs={'class': 'lg-tile s-hover'})]

    return types, wrongs


def mysocio_crawler(indexes, sleep=0.1, pattern='https://mysocio.ru/test/tolstikova/result/'):
    def data_to_line(ident, soctypes, wrongs):
        return '|'.join([str(ident),
                         '\t'.join(','.join(typ) for typ in soctypes),
                         '\t'.join(wrongs)])

    for index in indexes:
        html = requests.get(pattern + str(index)).text
        types, wrongs = parse_page(html)
        time.sleep(sleep)
        try:
            yield data_to_line(index, types, wrongs if wrongs else [])
        except TypeError:
            print(html)
            break


def line_to_data(line: str):
    ind, types, wrongs = line.split('|')
    return int(ind), [tuple(typ.split(',')) for typ in types.split('\t')], wrongs.split('\t')
