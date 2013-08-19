#! /usr/bin/env python
#coding=utf-8
import os
import sys
import datetime
import re
import time

def traverse(path, result):
    if os.path.isfile(path):
        analysis(path, result)
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp, result)

def analysis(path, result):
    print path
    log_type = get_log_type(path)
    if log_type == -1:
        return
    print path
    file_name = os.path.split(path)[1]
    log_file = open(path, 'r')
    try:
        for line in log_file:
            if log_type == 1:
                m = re.match(reg1, line)
            elif log_type == 2:
                m = re.match(reg2, line)
            else:
                continue
            
            if m is not None:
                if (len(m.groups()) != 16 and log_type == 1) or (len(m.groups()) != 17 and log_type == 2):
                    print '[error]' + line
                else:
                    record(m.groups(), result)
    finally:
        log_file.close()

def record(data, result):
    url = get_no_parameter_url(str(data[4]))
    request_code = int(data[6])
    dic_code = result.get(request_code)
    if dic_code is not None:
        temp = dic_code.get(str(url))
        if temp is None:
            dic_code[str(url)] = 1
        else:
            dic_code[str(url)] = temp + 1
    else:
        dic_code = {}
        dic_code[str(url)] = 1
    result[request_code] = dic_code

def get_no_parameter_url(url):
    url_reg = r'(.+)(\?.*)'
    m = re.match(url_reg, url)
    if m is None:
        return url
    else:
        return m.groups()[0]

def get_log_type(path):
    if re.match(eval('r\'' + nginx1 + '\''), path) is not None:
        return 1
    elif re.match(eval('r\'' + nginx2 + '\''), path) is not None:
        return 2
    else:
        return -1

def sort(data):
    ##{404:{url1:123, url2:762}}
    counter_cursor = 0
    url_cursor = ''
    result = []
    
    while(len(data) > 0):
        for key in data:
            temp = data[key]
            if temp > counter_cursor:
                counter_cursor = temp
                url_cursor = key
        result.append((url_cursor, counter_cursor))
        del data[url_cursor]
        counter_cursor = 0
        url_cursor = ''
    return result

def make_dir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def generate_report(log_time, result):
    report_file_dir = '/opt'
    report_file_name = report_file_dir + os.sep + log_time + '.html'
    make_dir(report_file_dir)
    try:
        result_file = open(report_file_name, 'w')
        result_file.writelines('<html>\n<head>\n<title>\n' + log_time + ' report\n</title>\n</head>\n<body>\n')
        for code in result:
            temp = result[code]
            result_after_sort = sort(temp)
            try:
                result_file.writelines('request_code:' + str(code) + '<br/>time:' + log_time)
                result_file.writelines('<table border="1">\n<tr><td>url</td><td>request times</td></tr>')
                for temp in result_after_sort:
                    url = temp[0]
                    count = temp[1]
                    result_file.writelines('<tr><td>' + url + '</td><td>' + str(count) + '</td></tr>\n')
            finally:
                result_file.writelines('</table>\n')
                result_file.flush()
    finally:
        result_file.writelines('</body>\n</html>')
        result_file.close()
                               
if __name__ == '__main__':
## get date of your want
    #log_time = datetime.date.today()
    log_time = '20130710'
    
## reg1\reg2 is regex for nginx log's data  
    reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'
    reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'

## nginx1\nginx2 is regex for nginx log's filename
    nginx1 = '(.*)((143\.115)|(143\.116))(.*?(' + log_time + '.*))'
    if log_time == datetime.date.today().strftime('%Y%m%d'):
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)activity\.access\.log$'
    else:
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)activity\.access\.log_' + log_time

## result of analysis   
    result = {}
## start analysis
    try:
        traverse('/opt/nginx_log', result)
        generate_report(log_time, result)
    finally:
        result = None
    
