#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import httplib
import traceback
import re


def loadSymbols():
    symbols = []
    f = open('../conf/symbols_us.txt', 'r')
    for l in f:
        symbols.append(l.lstrip().rstrip())
    return symbols
    # return ['SH601989']


def matchUrl(s):
    p = re.compile(r'"(http.*?)"')
    all = p.findall(s)
    if all is not None and len(all) > 0:
        return all[0]
    return None


def matchContent(s):
    p = re.compile(r'<div class="main">(.*?)</div>', re.S)
    a = p.findall(s)
    if a is not None and len(a) > 0:
        return a[0]
    return None


if __name__ == '__main__':
    symbols = loadSymbols()

    total = 0
    err = 0
    for symbol in symbols:
        try:
            page = 1
            maxPage = 100
            while True:
                if page >= maxPage:
                    break

                payload = {'symbol_id': symbol,
                           'count': 15,
                           'source': u'自选股新闻',
                           'page': page,
                           '_': 1444641818269}

                url = 'http://xueqiu.com/statuses/stock_timeline.json'

                headers = {
                    'Proxy-Connection': 'keep-alive',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'cache-control': 'no-cache',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-FirePHP-Version': '0.0.6',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                }

                cookies = {
                    'xq_a_token': 'e20acc1f64d812bf45403078dded25b5428b7979',
                    'xq_r_token': '74f94543ae9e1aecbf7403c4ec1a8d9a3982ff38;'
                }

                resp = requests.get(url, params=payload, headers=headers, cookies=cookies)
                ret = json.loads(resp.text)
                # print resp.text
                try:
                    maxPage = ret[u'maxPage']
                    if len(ret[u'list']) <= 0:
                        continue
                    page += 1
                    for oneNews in ret[u'list']:
                        total += 1
                        title = oneNews.get('title')
                        text = oneNews.get('text')
                        if title is None:
                            title = oneNews.get('text')
                        # print title, text
                        tUrl = matchUrl(text)
                        if matchUrl(text) is not None:
                            xueqiuUrl = 'http://xueqiu.com/mp/' + tUrl
                            print xueqiuUrl
                            response = requests.get(xueqiuUrl, headers=headers)
                            # print response.text
                            content = matchContent(response.text.encode('utf-8'))
                            # print content
                            if content is None:
                                err += 1
                except Exception, e:
                    traceback.print_exc()
            print '{}\t{}'.format(total, err)
        except Exception, e:
            traceback.print_exc()
