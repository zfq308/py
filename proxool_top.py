# -*- coding: cp936 -*-
import os
import operator
import httplib
import time
import sys

def top(data):
    global max_pool
    sort()
    if len(max_pool) > 0:
        for i in range(len(max_pool)):
            if max_pool[i]['served'] < data['served']:
                max_pool[i] = data
                break
    else:
        max_pool.append(data)
    
def sort():
    global max_pool
    temp_pool = []
    index = None
    for t in range(len(max_pool)):
        for i in range(len(max_pool)):
            if index is None:
                index = max_pool[i]
            else:
                if max_pool[i]['served'] > index['served']:
                    index = max_pool[i]
                else:
                    pass
        temp_pool.append(index)
        del max_pool[i]
        index = None
    max_pool = temp_pool
                       
def trim(zstr):
    ystr=zstr.lstrip()
    ystr=ystr.rstrip()
    ystr=ystr.strip()
    return ystr

def str_to_date(s):
    t = time.strptime( s, "%Y-%m-%d %H:%M:%S" )
    return t
    
def get_lines(html):
    html = html.split('</form>')
    content = html[1].split('</body>')[0];
    lines = content.split('</br>')
    for index in range(len(lines) - 1):
        line = trim(lines[index])
        lines[index] = line
        index += 1
    return lines[0 : len(lines) - 1]

def go(total):
    max_pool = None
    headers = {'Authorization':'Basic YWN0aXZpdHlsb2c6MTEzem8hIyUhQHhjdnVubDEzMms1'}
    #'10.127.64.209','10.127.64.224','10.127.64.195','10.127.64.196','10.127.64.203','10.127.64.204',,'10.11.154.96','10.11.154.97','10.11.55.25'
    ips = ['10.127.64.210','10.127.64.209','10.127.64.224','10.127.64.195','10.127.64.196','10.127.64.203','10.127.64.204','10.11.154.96','10.11.154.97','10.11.55.25']
    for ip in ips:
        print 'start sync ' + ip
        httpconn = httplib.HTTPConnection(ip)
        httpconn.request('GET','/background/testSession20120110/shell.jsp?filepath=/opt/proxoolLog/&filename=proxoolinfo.log&num=' + str(total),headers=headers)
        result = httpconn.getresponse()
        lines = get_lines(result.read())
        count = 0
        for line in lines:
            count += 1
            data = trim(line.split('.')[1]).split(',')
            alias = data[0].split(':')
            served = data[1].split(':')
            refused = data[2].split(':')
            averageActiveTime = data[3].split(':')
            start, end = data[4].split('--')
            temp = {'server_ip':ip, 'alias':alias[1], 'served':int(served[1]), 'refused':refused[1], 'averageActiveTime':averageActiveTime[1], 'start':start, 'end':end}
            if (str_to_date(start) >= str_to_date('2012-11-15 06:00:00')) and (str_to_date(start) <= str_to_date('2012-11-16 00:00:00')):
                if max_pool is None:
                    max_pool = temp
                else:
                    if max_pool['served'] < temp['served']:
                        max_pool = temp
        print 'total-' + str(count)

        
if __name__ == '__main__':
    go(raw_input('请输入行数：'))