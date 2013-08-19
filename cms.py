#! /usr/bin/env python
#coding=utf-8
import os
import urllib

old_addr = ['http://ldj.changyou.com/s2011/ghsp_2/index.shtml','http://ldj.changyou.com/s2011/ghsp_2/index_1.shtml']

def getHtml(url):
    return urllib.urlopen(url).read()

if __name__ == '__main__':
    for addr in old_addr:
        str = getHtml(addr)
        print len(str.split('<a href='))
        print str.split('·<a href=')[1:len(str.split('·<a href='))-1]
