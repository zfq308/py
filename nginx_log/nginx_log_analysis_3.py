#! /usr/bin/env python
#coding=utf-8
import os
import sys
import datetime
import re
import time
import webbrowser

url_reg = r'(.+)(\?.*)'
error_count = 0
success_count = 0

# 遍历日志目录，并返回处理结果
def traverse(path, result):
    if os.path.isfile(path):
        analysis(path, result)
        print path
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp, result)

# 分析日志文件
def analysis(path, result):
    global error_count
    global success_count
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
    c1 = 0
    c2 = 0
    try:
        for line in file:
            if 'tlJxws' in line:
                pass
            else:
                continue
            if log_type == 1:
                m = re.match(reg1, line)
            else:
                m = re.match(reg2, line)
            # 不合要求的日志行
            if m == None:
                print line
            else:
                # 不合要求的日志行
                if (len(m.groups()) != 16 and log_type == 1) or (len(m.groups()) != 17 and log_type == 2):
                    c1 += 1
                    print '[error]' + m.groups()
                else:
                    if record(m.groups(), result) == 0:
                        c1 += 1
                    else:
                        c2 += 1
        print str(c1) + '-' + str(c2)
        error_count += c1
        success_count += c2
    finally:
        file.close()

# 记录日志行中的数据到result
def record(data, result):
    ip = data[0]
    
    ## result {'ip':times}
    times = result.get(ip)
    if times is not None:
            result[ip] = times + 1
    else:
            result[ip] = 1
    return 1

# 删除url中的参数
def get_url(url):
    m = re.match(url_reg, url)
    if m is None:
        return url
    else:
        return m.groups()[0]

# 按照访问次数将结果排序
def sort(result):
    result_after_sort = []
    max_count = 0
    ip = ''
    while(len(result) > 0):
        for key in result:
            temp = result[key]
            if temp > max_count:
                max_count = temp
                ip = key
        result_after_sort.append((ip,max_count))
        del result[ip]
        max_count = 0
        ip = ''
    return result_after_sort

def make_dir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)
    
def get_input_time():
    try:
        print u'请输入日志的日期，格式为yyyyMMdd，例如20120101\n-->yyyyMMdd\n-->'
        input_time = str(input())
        log_time = datetime.datetime.strptime(input_time, '%Y%m%d')
        return log_time
    except SyntaxError:
        print 'default time is today\n'
        return datetime.date.today()
    except ValueError:
        print u'输入格式不正确，请重试，格式为:yyyyMMdd，例如：20120101\n'
        return get_input_time()
                               
if __name__ == '__main__':
    log_time = get_input_time()
    
    nginx1 = '(.*)((143\.115)|(143\.116))(.*?(' + log_time.strftime('%Y%m%d') + '.*))'
    reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'

    if log_time.strftime('%Y%m%d') == datetime.date.today().strftime('%Y%m%d'):
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)$'
    else:
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)' + log_time.strftime('%Y-%m-%d')
    
    reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'

    result = {}
    traverse('d:\\opt\\nginx_log', result)
    if len(result.keys()) == 0:
        print 'sorry, no data'
    else:
        result_sort = sort(result)
        i = 0
        while(i < 30):
                print str(result_sort[i]) + '\n'
                i += 1
		
    
