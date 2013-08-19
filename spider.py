#! /usr/bin/env python
#coding=utf-8
import urllib
import os
import datetime
import random

imageType = ['.jpg', '.jpeg', '.gif', '.png']

class Page:
    url = ''
    html = ''
    links = []

def getstr(n): 
	al=list('abcdefghijklmnopqrstuvwxyz') 
	st='' 
	for i in range(n): 
		index = random.randint(0, len(al)-1) 
		st = st + al[index] 
		del al[index] 
	return st

def getHtml(page):
    page.html = urllib.urlopen(page.url).read()

def getLinks(page):
    #按行进行分段
    stringsByLineSep = page.html.split(os.linesep)
    for stringByLineSep in stringsByLineSep:
        #按空格进行分段
        stringsBySpace = stringByLineSep.split(' ')
        for stringBySpace in stringsBySpace:
            #按双引号进行分段
            stringsByDoublequot = stringBySpace.split('\"')
            for stringByDoublequot in stringsByDoublequot:
                if(isLink(stringByDoublequot)):
                    #print stringByDoublequot
                    save(stringByDoublequot)

def isLink(string):
    if string.startswith('http'):
        return True
    else:
        return False

def save(link):
    for type in imageType:
        if link.endswith(type):
            filename = str(getstr(5) + str(datetime.datetime.now().microsecond) + link.split('/')[-1])
            print filename
            urllib.urlretrieve(link, filename)
            break
            
if __name__ == '__main__':
    os.chdir('E:' + os.sep + 'Downloads')
    page = Page()
    page.url = 'http://image.baidu.com/i?word=12121&opt-image=on&cl=2&lm=-1&ct=201326592&ie=gbk'
    getHtml(page)
    # print(page.html)
    getLinks(page)
