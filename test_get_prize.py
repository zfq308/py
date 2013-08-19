import os
import operator
import MySQLdb
import httplib
import time
import sys

def trim(zstr):
    ystr=zstr.lstrip()
    ystr=ystr.rstrip()
    ystr=ystr.strip()
    return ystr

def get_data(line):
    data = line.split(',')
    times = data[4].split('--')
    start = times[0]
    end = times[1]
    served = data[1].split(':')[1]
    return start, end, served

def exist(data, ip, conn):
    sql = "select 1 from t_proxool where start = %s and end = %s and ip = %s"
    cursor = conn.cursor()
    count = cursor.execute(sql, (data[0], data[1], ip))
    if count > 0:
        return True
    else:
        return False

def insert(data, conn):
    #sql = "insert into t_ty_friends_level (cn_master, lvl) values (%s, %s)"
    sql = 'INSERT INTO t_ty_friends_level (cn_master, lvl) VALUES (%s, %s) ON DUPLICATE KEY UPDATE lvl = 100'
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    
def save(data, conn):
    #sql = "insert into t_tyfriends_result (cn_master, lvl) values (%s, %s)"
    sql = 'INSERT INTO t_tyfriends_result (cn_master, cdkey) VALUES (%s, %s) ON DUPLICATE KEY UPDATE cdkey = %s'
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

def update(data, ip, conn):
    sql = "update t_proxool set served = %s where start = %s and end = %s and served < %s and ip = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (data[2], data[0], data[1], data[2], ip))
    conn.commit()

def test_get_prize(total):
    conn = MySQLdb.connect(host='localhost', user='root',passwd='Uat123', db='cyou')
    index = 1
    while index <= total:
        insert((str(index)+'@changyou.com', 100), conn)
        httpconn = httplib.HTTPConnection('127.0.0.1')
        httpconn.request('GET','/tyfriends/jsp/get_prize.jsp?cn_master=' + str(index) + '@changyou.com')
        result = httpconn.getresponse()
        html = trim(result.read())
        save((str(index)+'@changyou.com', html, html), conn)
        print str(index) + '--' + trim(html)
        index += 1
    conn.close()
    
if __name__ == '__main__':
    test_get_prize(100)
