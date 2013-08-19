import os
import operator
import MySQLdb
import httplib
import time
import sys

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

def insert(data, ip, conn):
    sql = "insert into t_proxool (start, end, served, ip) values (%s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, (data[0], data[1], data[2], ip))
    conn.commit()

def update(data, ip, conn):
    sql = "update t_proxool set served = %s where start = %s and end = %s and served < %s and ip = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (data[2], data[0], data[1], data[2], ip))
    conn.commit()

if __name__ == '__main__':
    total = str(input('请输入获取获取的日志行数:'))
    flag = True
    headers = {'Authorization':'Basic YWN0aXZpdHlsb2c6MjEzem8hIyUhQHhjdnVubDEzMms1'}
    conn = MySQLdb.connect(host='localhost', user='root',passwd='Uat123', db='cyou')
    ips = ['10.127.64.209','10.127.64.224','10.127.64.195','10.127.64.196','10.127.64.203','10.127.64.204','10.127.64.210','10.11.154.96','10.11.154.97']
    for ip in ips:
        flag = True
        print ip
        httpconn = httplib.HTTPConnection(ip)
        httpconn.request('GET','/background/logMonitor/shell.jsp?filepath=/opt/proxoolLog/&filename=proxoolinfo.log&num=' + total,headers=headers)
        result = httpconn.getresponse()
        html = result.read().split('</br>')
        for line in html:
            if(operator.contains(line, 'alias:activity_new,served:')):
                #print '[success]' + line
                data = get_data(line)
                if flag:
                    print data
                    flag = False
                if(exist(data, ip, conn) is True):
                    update(data, ip, conn)
                else:
                    insert(data, ip, conn)
            else:
                pass
                #print '[error]' + line
    conn.close()
#select * from t_proxool where start >= '2012-05-24 06:00:00' and end <= '2012-05-25 00:00:00' ORDER BY served desc limit 20
