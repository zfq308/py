#! /usr/bin/env python
#coding=utf-8
import os
import sys
import datetime
import re
import time
import webbrowser

url_reg = r'(.+)(\?.*)'

def traverse(path, result):
    if os.path.isfile(path):
        analysis(path, result)
        print path
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp, result)

def analysis(path, result):
    if re.match(eval('r\'' + nginx1 + '\''), path) is not None:
        log_type = 1
        print path
    elif re.match(eval('r\'' + nginx2 + '\''), path) is not None:
        log_type = 2
        print path
    else:
        return
    file_name = os.path.split(path)[1]
    file = open(path, 'r')
    try:
        for line in file:
            if(special_url not in line):
                continue
            if log_type == 1:
                m = re.match(reg1, line)
            else:
                m = re.match(reg2, line)
            if m == None:
                print line
            else:
                if (len(m.groups()) != 16 and log_type == 1) or (len(m.groups()) != 17 and log_type == 2):
                    c1 += 1
                    print '[error]' + m.groups()
                else:
                    record(m.groups(), result)
    finally:
        file.close()

def record(data, result):
    remote_ip = str(data[0])
    hour, min = int(str(data[2]).split(':')[1]), int(str(data[2]).split(':')[2])
    
    if (hour == 19) and (min >= 30 and min <= 50):
        times = result.get(remote_ip)
        if times is not None:
            times = times + 1
        else:
            times = 1
        result[remote_ip] = times

def get_url(url):
    m = re.match(url_reg, url)
    if m is None:
        return url
    else:
        return m.groups()[0]

def make_dir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def generate_result_file(log_time, result):
    report_file_name = '/opt/log1/nginx_log_analysis_result/'+ os.sep + special_file_name + '_' + log_time + '.log'
    result_file = open(report_file_name, 'w')
    try:
        result_file.writelines(special_url + ',' + log_time + '\n')
        for ip in result:
            times = result[ip]
            if times < time_baseline:
                continue
            try:
                result_file.writelines(ip + ',' + str(times) + '\n')
            finally:
                result_file.flush()
    finally:
        result_file.close()
    ## webbrowser.open(report_file_name)
    
def get_input_time():
    try:
        print u'which date(default:today), format[yyyyMMdd]:'
        input_time = str(input())
        log_time = datetime.datetime.strptime(input_time, '%Y%m%d')
        return log_time
    except SyntaxError:
        print 'default time is today\n'
        return datetime.date.today()
    except ValueError:
        print u'date format error, format:yyyyMMdd\n'
        return get_input_time()
                               
if __name__ == '__main__':
    log_time = get_input_time()
    special_file_name = 'yhmxPutCode'
    special_url = '/yhmxPutCode/lot/lotManager.jsp'
    time_baseline = 100

    nginx1 = '(.*)((143\.115)|(143\.116))(.*?(' + log_time.strftime('%Y%m%d') + '.*))'
    reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'
    reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'
    if log_time.strftime('%Y%m%d') == datetime.date.today().strftime('%Y%m%d'):
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)$'
    else:
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)' + log_time.strftime('%Y-%m-%d')
    
    result = {}
    traverse('/opt/log1/nginx_log', result)
    if len(result.keys()) == 0:
        print 'no data'
    else:
        generate_result_file(log_time.strftime('%Y%m%d'), result)
    
