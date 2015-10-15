__author__ = 'kangshuai'

import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def loadSymbols():
    symbols = []
    f = open('../conf/symbols_sh.txt', 'r')
    for l in f:
        symbols.append(l.lstrip().rstrip())
    return symbols

def match(text):
    import re
    p = re.compile(r'id="content">(.*?)</div>', re.S)
    return p.findall(text)[0]

if __name__ == '__main__':
    total = 0
    for symbol in loadSymbols():
        page = 1
        maxPage = 1
        while True:
            if page > maxPage:
                break
            url = 'http://news.10jqka.com.cn/stock_mlist/{}_1_-1_1_{}/'.format(symbol, page)
            print url
            resp = requests.get(url)
            page += 1
            text = resp.text
            tree = ET.fromstring(text.encode('utf-8'))
            maxPage = int(tree.find('pages').text)
            for ele in tree.iterfind('pageItems/item'):
                seq = ele.find('seq').text
                title = ele.find('title').text
                ctime = ele.find('ctime').text
                source = ele.find('source').text
                url = ele.find('url').text
                total += 1
                # print seq, title, ctime, source, url, match(requests.get(url).text)
        print total, symbol