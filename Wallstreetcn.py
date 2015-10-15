__author__ = 'kangshuai'

import requests
import json
import traceback


def loadSymbols():
    symbols = []
    f = open('../conf/symbols_sh.txt', 'r')
    for l in f:
        symbols.append(l.lstrip().rstrip())
    return symbols


def match(text):
    import re
    p = re.compile(r'<div class="content article-content">(.*?)</div>', re.S)
    articleContent = p.findall(text)[0]
    p1 = re.compile(r'(.*?)<p class="hide-for-app">.*?</p>', re.S)
    return p1.findall(articleContent)[0]


if __name__ == '__main__':
    total = 0
    for symbol in loadSymbols():
        url = 'http://api.buzz.wallstreetcn.com/v2/posts?type=news&status=published&cid=1000002&tag={}&order=-created_at&limit=10&page=1'.format(
            symbol)
        while True:
            try:
                resp = requests.get(url)
                text = resp.text
                ret = json.loads(resp.text)
                results = ret['results']
                for result in results:
                    total += 1
                    url = result['url']
                    print total, symbol, result['id'], result['title'], url
                    # print match(r.text)
                paginator = ret['paginator']
                if paginator is None:
                    break
                next = paginator['next']
                last = paginator['last']
                if last == next:
                    break
                url = next
            except Exception, e:
                traceback.print_exc()
