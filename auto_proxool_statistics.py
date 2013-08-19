# -*- coding: cp936 -*-
import os
import operator
import MySQLdb
import httplib
import time
import sys

def into_db(server_ip, lines, batch_line_limit, conn):
    count = 0
    buffer = []
    for line in lines:
        count += 1
        data = trim(line.split('.')[1]).split(',')
        alias = data[0].split(':')
        served = data[1].split(':')
        refused = data[2].split(':')
        averageActiveTime = data[3].split(':')
        start, end = data[4].split('--')
        temp = {'server_ip':server_ip, 'alias':alias[1], 'served':served[1],
                'refused':refused[1], 'averageActiveTime':averageActiveTime[1], 'start':start, 'end':end}
        if(exist(temp, conn) is False):
            buffer.append((temp['server_ip'], temp['alias'], temp['served'], temp['refused'], temp['averageActiveTime'], temp['start'], temp['end']))
        if count%batch_line_limit == 0:
            insert(tuple(buffer), conn)
            print server_ip + ' : ' + str(count)
            buffer = []
    insert(buffer, conn)
    print server_ip + ' : ' + str(count)
    buffer = ()
        
def insert(temp, conn):
    sql = "insert into t_proxool_monitor (server_ip, alias, served, refused, averageActiveTime, start, end) values (%s, %s, %s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.executemany(sql, temp)
    conn.commit()

def exist(temp, conn):
    sql = "select 1 from t_proxool_monitor t where t.server_ip = %s and t.alias = %s and t.start = %s"
    cursor = conn.cursor()
    count = cursor.execute(sql, (temp['server_ip'], temp['alias'], temp['start']))
    if count > 0:
        return True
    else:
        return False                  

def trim(zstr):
    ystr=zstr.lstrip()
    ystr=ystr.rstrip()
    ystr=ystr.strip()
    return ystr

def get_lines(html):
    html = html.split('</form>')
    content = html[1].split('</body>')[0];
    lines = content.split('</br>')
    for index in range(len(lines) - 1):
        line = trim(lines[index])
        lines[index] = line
        index += 1
    return lines[0 : len(lines) - 1]

def go(total, batch_line_limit):
    print 'start get connection...'
    conn = MySQLdb.connect(host='localhost', user='root',passwd='Uat123', db='cyou_new')
    print 'connect db done...'
    headers = {'Authorization':'Basic YWN0aXZpdHlsb2c6MTEzem8hIyUhQHhjdnVubDEzMms1'}
    ips = ['10.127.64.209','10.127.64.224','10.127.64.195','10.127.64.196','10.127.64.203','10.127.64.204','10.127.64.210','10.11.154.96','10.11.154.97','10.11.55.25']
    for ip in ips:
        print 'start sync ' + ip
        httpconn = httplib.HTTPConnection(ip)
        httpconn.request('GET','/background/testSession20120110/shell.jsp?filepath=/opt/proxoolLog/&filename=proxoolinfo.log&num=' + str(total),headers=headers)
        result = httpconn.getresponse()
        lines = get_lines(result.read())
        into_db(ip, lines, batch_line_limit, conn)
    conn.close()
        
if __name__ == '__main__':
    go(sys.argv[1], int(sys.argv[2]))
