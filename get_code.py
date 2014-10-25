#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import HTMLParser
import urlparse
import urllib, urllib2
import cookielib
import time

result = {}

def showDealMsg(data):
    prize = ['雷','蛇','地','狱','狂','杀','人','鲸','帝','王','蟒'
             ,'黑','寡','妇','圣','甲','虫','徽','章','金','银'
             ,'A','K','4','7','黄','I','P','H','O','N','E'
             ,'D','套','装']
    if result.get(prize[int(data['putword']) - 1]) is None:
        result[prize[int(data['putword']) - 1]] = 1
    else:
        result[prize[int(data['putword']) - 1]] += 1
    
if __name__ == '__main__':
    
    host_url = 'http://activity.changyou.com'
    login_url = 'http://activity.changyou.com/zdfindword/loginDeal.jsp'
    checkcode_url = 'http://activity.changyou.com/extracode/imgcode.jsp?random_mark=1'
    prize_url = 'http://activity.changyou.com/zdfindword/dealfloat.jsp?callback=showDealMsg'
    get_prize_url = 'http://activity.changyou.com/zdfindword/index.jsp'
    get_session_url = 'http://activity.changyou.com/zdfindword/getSession.jsp'
    account = {'cn':'cr7_2012@changyou.com', 'password':'abc1234', 'code':''}

    cj = cookielib.LWPCookieJar() 
    cookie_support = urllib2.HTTPCookieProcessor(cj) 
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
    urllib2.install_opener(opener)

    print 'opener init'
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', 
               'Content-Type:text/html' : 'charset=utf-8', 'Connection' : 'keep-alive'}

    request = urllib2.Request(checkcode_url, None, headers)
    response = urllib2.urlopen(request)
    check_image = open('/home/spruce/1.jpeg', 'w+b')
    check_image.write(response.read())
    check_image.close()
    
    code = raw_input()
    
    account['code'] = code
    login_data = urllib.urlencode(account)
    print login_data
    
    request = urllib2.Request(login_url, login_data, headers)
    response = urllib2.urlopen(request)
    text = response.read() 
    print text

    i = 0
    while True:
        i += 1
        try:
            if i % 100 == 0:
                print str(result)
                request = urllib2.Request(get_session_url, None, headers)
                response = urllib2.urlopen(request)
                text = response.read()
                if '511433355' in text:
                    pass
                else:
                    print 'not login'
                    
            request = urllib2.Request(prize_url, None, headers)
            response = urllib2.urlopen(request)
            text = response.read() 
            eval(text.lstrip().rstrip())

            request = urllib2.Request(get_prize_url, None, headers)
            response = urllib2.urlopen(request)
        except Exception, e:
            print e
        finally:
            pass
