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
    link = get_url(str(data[4]))
    request_code = int(data[6])
    response_time = 0.00000

    if(data[13] == '-'):
        return 0
    else:
        try:
            for t in data[13].split(','):
                response_time += float(t)
        except Exception, e:
            print e
##            print data
            return 0

    dic_code = result.get(request_code)
    if float(response_time) < 1.0:
        return
    if dic_code is not None:
        temp = dic_code.get(str(link))
        if temp is None:
            dic_code[str(link)] = (1, float(response_time))
        else:
            response_time += temp[1]
            dic_code[str(link)] = (temp[0] + 1, response_time)
    else:
        dic_code = {}
        dic_code[str(link)] = (1, float(response_time))
    result[request_code] = dic_code
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
    url_cursor = ''
    
    while(len(result) > 0):
        for key in result:
            temp = result[key]
            if int(temp[0]) > max_count:
                max_count = temp[0]
                url_cursor = key
        result_after_sort.append((url_cursor, result[url_cursor][0], result[url_cursor][1]))
        del result[url_cursor]
        max_count = 0
        url_cursor = ''
    return result_after_sort

def make_dir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)

def generate_result_file(log_time, result):
    report_file_name = 'd:/opt/activity/'+ os.sep + log_time + '.html'
    ##    make_dir(file_path_head)
    try:
        result_file = open(report_file_name, 'w')
        result_file.writelines('<html>\n<head>\n<title>\n' + log_time + ' report\n</title>\n</head>\n<body>\n')
        for code in result:
            temp = result[code]
            result_after_sort = sort(temp)
            try:
                result_file.writelines('request_code:' + str(code) + '<br/>time:' + log_time)
                result_file.writelines('<table border="1">\n<tr><td>url</td><td>request times</td><td>avg_response_time</td></tr>')
                for temp in result_after_sort:
                    url = temp[0]
                    count = temp[1]
                    sum_time = temp[2]
                    result_file.writelines('<tr><td>' + url + '</td><td>' + str(count) + '</td><td>' + str(sum_time/count) + '</td></tr>\n')
            finally:
                result_file.writelines('</table>\n')
                result_file.flush()
    finally:
        result_file.writelines('[err-count]' + str(error_count) + ', [success-count]' + str(success_count))
        result_file.writelines('</body>\n</html>')
        result_file.close()
    webbrowser.open(report_file_name)
    
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
   
    nginx1 = '(.*)((143\.115)|(143\.116))(.*?)'
	nginx2 = '(.*)((49\.112)|(49\.109))(.*?)'
    reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'
    reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'

    result = {}
    traverse('d:/opt/activity/', result)
    if len(result.keys()) == 0:
        print 'sorry, no data'
    else:
        generate_result_file(log_time.strftime('%Y%m%d'), result)
    
