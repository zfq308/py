#! /usr/bin/env python
#coding=utf-8
import os
import sys
import datetime
import re
import time
import webbrowser
from ftplib import FTP
import string
import socket

url_reg = r'(.+)(\?.*)'

error_count = 0
success_count = 0

class MYFTP:
	def __init__(self, hostaddr, username, password, remotedir, port=21):
		self.hostaddr = hostaddr
		self.username = username
		self.password = password
		self.remotedir  = remotedir
		self.port     = port
		self.ftp      = FTP()
		self.file_list = []
		# self.ftp.set_debuglevel(2)
	def __del__(self):
		self.ftp.close()
		# self.ftp.set_debuglevel(0)
	def login(self):
		ftp = self.ftp
		try: 
			timeout = 60
			socket.setdefaulttimeout(timeout)
			ftp.set_pasv(True)
			print u'开始连接到 %s' %(self.hostaddr)
			ftp.connect(self.hostaddr, self.port)
			print u'成功连接到 %s' %(self.hostaddr)
			print u'开始登录到 %s' %(self.hostaddr)
			ftp.login(self.username, self.password)
			print u'成功登录到 %s' %(self.hostaddr)
			debug_print(ftp.getwelcome())
		except Exception:
			print u'连接或登录失败'
		try:
			ftp.cwd(self.remotedir)
		except(Exception):
			print u'切换目录失败'

	def is_same_size(self, localfile, remotefile):
		try:
			remotefile_size = self.ftp.size(remotefile)
		except:
			remotefile_size = -1
		try:
			localfile_size = os.path.getsize(localfile)
		except:
			localfile_size = -1
		debug_print('localfile_size:%d  remotefile_size:%d' %(localfile_size, remotefile_size),)
		if remotefile_size == localfile_size:
		 	return 1
		else:
			return 0
	def download_file(self, localfile, remotefile, nginx1, nginx2):  
                if re.match(eval('r\'' + nginx1 + '\''), remotefile) is not None:
                    pass
                elif re.match(eval('r\'' + nginx2 + '\''), remotefile) is not None:
                    pass
                else:
                    print remotefile
                    return
		if self.is_same_size(localfile, remotefile):
		 	debug_print(u'%s 文件大小相同，无需下载' %localfile)
		 	return
		else:
			debug_print(u'>>>>>>>>>>>>下载文件 %s ... ...' %localfile)
		#return
		file_handler = open(localfile, 'wb')
		self.ftp.retrbinary(u'RETR %s'%(remotefile), file_handler.write)
		file_handler.close()

	def download_files(self, localdir='./', remotedir='./', nginx1='', nginx2=''):
		try:
			self.ftp.cwd(remotedir)
		except:
			debug_print(u'目录%s不存在，继续...' %remotedir)
			return
		if not os.path.isdir(localdir):
			os.makedirs(localdir)
		debug_print(u'切换至目录 %s' %self.ftp.pwd())
		self.file_list = []
		self.ftp.dir(self.get_file_list)
		remotenames = self.file_list
		#print(remotenames)
		#return
		for item in remotenames:
			filetype = item[0]
			filename = item[1]
			local = os.path.join(localdir, filename)
			if filetype == 'd':
				self.download_files(local, filename, nginx1, nginx2)
			elif filetype == '-':
				self.download_file(local, filename, nginx1, nginx2)
		self.ftp.cwd('..')
		debug_print(u'返回上层目录 %s' %self.ftp.pwd())
	def upload_file(self, localfile, remotefile):
		if not os.path.isfile(localfile):
			return
		if self.is_same_size(localfile, remotefile):
		 	debug_print(u'跳过[相等]: %s' %localfile)
		 	return
		file_handler = open(localfile, 'rb')
		self.ftp.storbinary('STOR %s' %remotefile, file_handler)
		file_handler.close()
		debug_print(u'已传送: %s' %localfile)
	def upload_files(self, localdir='./', remotedir = './'):
		if not os.path.isdir(localdir):
			return
		localnames = os.listdir(localdir)
		self.ftp.cwd(remotedir)
		for item in localnames:
			src = os.path.join(localdir, item)
			if os.path.isdir(src):
				try:
					self.ftp.mkd(item)
				except:
					debug_print(u'目录已存在  %s' %item)
				self.upload_files(src, item)
			else:
				self.upload_file(src, item)
		self.ftp.cwd('..')

	def get_file_list(self, line):
		ret_arr = []
		file_arr = self.get_filename(line)
		if file_arr[1] not in ['.', '..']:
			self.file_list.append(file_arr)
			
	def get_filename(self, line):
		pos = line.rfind(':')
		while(line[pos] != ' '):
			pos += 1
		while(line[pos] == ' '):
			pos += 1
		file_arr = [line[0], line[pos:]]
		return file_arr

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
        
def debug_print(s):
	print s
        
# 记录日志行中的数据到result
def record(data, result):
    link = get_url(str(data[4]))
    request_code = int(data[6])
    response_time = 0.00000

    if data[13] == '-':
        return 0
    try:
        for t in data[13].split(','):
            response_time += float(t)
    except Exception, e:
##        print e
##        print data
        return 0

    dic_code = result.get(request_code)
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
    report_file_name = 'd:/opt/nginx_report/'+ os.sep + log_time + '.html'
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
        print 'input date (format:yyyyMMdd):'
        input_time = str(input())
        log_time = datetime.datetime.strptime(input_time, '%Y%m%d')
        return log_time
    except SyntaxError:
        print 'default time is today\n'
        return datetime.date.today()
    except ValueError:
        print 'format of your inputed date is wrong!'
        return get_input_time()
                               
if __name__ == '__main__':
    ## get date of your want
    log_time = get_input_time()
    
    ## reg1\reg2 is regex for nginx log's data  
    reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'
    reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'
    
    ## nginx1\nginx2 is regex for nginx log's filename
    nginx1 = '(.*)((143\.115)|(143\.116))(.*?(' + log_time.strftime('%Y%m%d') + '.*))'
    if log_time.strftime('%Y%m%d') == datetime.date.today().strftime('%Y%m%d'):
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)activity\.access\.log$'
    else:
        nginx2 = '(.*)((49\.112)|(49\.109))(.*?)activity\.access\.log_' + log_time.strftime('%Y-%m-%d')

    ## nginx1\nginx2 is regex for nginx log's filename
    nginx_log_name_1 = '.*?(' + log_time.strftime('%Y%m%d') + '.*)'
    if log_time.strftime('%Y%m%d') == datetime.date.today().strftime('%Y%m%d'):
        nginx_log_name_2 = 'activity\.access\.log$'
    else:
        nginx_log_name_2 = 'activity\.access\.log_' + log_time.strftime('%Y-%m-%d')

    # 配置如下变量
    hostaddr = '10.11.148.29' # ftp地址
    username = 'ldjlog1' # 用户名
    password = 'JakwSYInq0yAZV' # 密码
    port  =  8021   # 端口号 
    rootdir_local  = 'D:/opt/nginx_log' # 本地目录
    rootdir_remote = '/nginx_log/'          # 远程目录
    f = MYFTP(hostaddr, username, password, rootdir_remote, port)
    f.login()
    f.download_files(rootdir_local, rootdir_remote, nginx_log_name_1, nginx_log_name_2)

    ## result of analysis   
    result = {}
    
    ## start analysis
    traverse('D:/opt/nginx_log/', result)
    
    ## if result is not null, take the result into filesystem.
    if len(result.keys()) == 0:
        print 'sorry, result of analysis is None'
    else:
        generate_result_file(log_time.strftime('%Y%m%d'), result)
    
