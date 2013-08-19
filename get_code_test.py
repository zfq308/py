#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import HTMLParser
import urlparse
import urllib, urllib2
import cookielib
import time

def showDealMsg(data):
    prize = ['雷','蛇','地','狱','狂','杀','人','鲸','帝','王','蟒','黑','寡','妇','圣','甲','虫','徽','章','金','银','A','K','4','7','黄','I','P','H','O','N','E','D','套','装']
    if data['putswitch'] == '1':
        print prize[int(data['putword'])]
    

if __name__ == '__main__':

    login_url = 'http://activity.changyou.com/zdfindword/loginDeal.jsp'
    checkcode_url = 'http://activity.changyou.com/extracode/imgcode.jsp?random_mark=1'
    prize_url = 'http://activity.changyou.com/zdfindword/dealfloat.jsp?callback=showDealMsg'
    get_session_url = 'http://activity.changyou.com/zdfindword/getSession.jsp'
    account = {'cn':'15110130276', 'password':'Uat123', 'code':''}

    cj = cookielib.LWPCookieJar() 
    cookie_support = urllib2.HTTPCookieProcessor(cj) 
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
    urllib2.install_opener(opener)
    
    check_image = open('/home/spruce/1.jpeg', 'w+b')
    check_image.write(opener.open(checkcode_url, None).read())
    check_image.close()
    
    code = raw_input()
    
    account['code'] = code
    login_data = urllib.urlencode(account)
    print login_data
    
    text = opener.open(login_url, login_data).read()
    print text

    while True:
        time.sleep(0.01)
        try:
            text = opener.open(get_session_url, None).read()
            if '501900339' in text.lstrip().rstrip():
                pass
            else:
                print 'not login'
            
            text = opener.open(prize_url, None).read()
            eval(text.lstrip().rstrip())
        except Exception, e:
            print e
        finally:
            pass
# function go() {$.ajax({url:'http://activity.changyou.com/zdfindword/dealfloat.jsp?callback=showDealMsg', type:'post', success:function(data){}});}for (var i = 0; i<1000000; i+=100)setTimeout('go()', 100+i);
