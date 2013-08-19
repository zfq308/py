import sys
import os
import operator
import MySQLdb
import httplib
import time


def trim(zstr):
    ystr=zstr.lstrip()
    ystr=ystr.rstrip()
    ystr=ystr.strip()
    return ystr
    
def save(data, conn):
    #sql = "insert into t_tyfriends_result (cn_master, lvl) values (%s, %s)"
    sql = 'INSERT INTO t_tyfriends_result (cn_master, cdkey) VALUES (%s, %s) ON DUPLICATE KEY UPDATE cdkey = %s'
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()


def get_prize(total):
    conn = MySQLdb.connect(host='localhost', user='root',passwd='Uat123', db='cyou')
    index = 0
    while index < total:
        httpconn = httplib.HTTPConnection('127.0.0.1')
        httpconn.request('GET','/tyfriends/jsp/lottery.jsp?cn_master=' + str(index) + '@changyou.com')
        result = httpconn.getresponse()
        html = trim(result.read())
        html = html.split(',')[0]
        print str(index) + '--' + trim(html)
        save((str(index)+'@changyou.com', html, html), conn)
        index += 1
    conn.close()

    
if __name__ == '__main__':
    get_prize(input('total test times:'))
