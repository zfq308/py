import os
import sys
import re

reg1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-"\s"(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"'
reg2 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?#ip)\s-\s(.*?)\s(\[.*\])(?#time)\s"(\b\w*\b)\s(.*?)(?#activity_link)\s(.*?)(?#protocol_type)"\s(\d{3})(?#request_code)\s(\d{1,10})(?#body_bytes_sent)\s"(.*?)(?#refer)"\s"(.*?)(?#http_user_agent)"\s"(.*?)""(.*?(?#ip)(?#ip))"\s"-""(.*(?#upstream_status))"\s"(.*?)(?#upstream_response_time)"\s"(.*)"\s"(.*?)(?#request_time)"\s"(.*)"'
result = {}

def traverse(path):
	if os.path.isfile(path):
		print path
		analysis(path)
	else:
	    for temp in os.listdir(path):
		traverse(path + os.sep + temp)

def analysis(path):
	log_reg = ''
	if '143.115' in path or '143.116' in path:
		log_reg = reg1
	else:
		log_reg = reg2
		
	log = open(path)
	try:
		for line in log:
			if '/client/ip.jsp' in line or '/favicon.ico' in line:
				pass
			else:
				m = re.match(log_reg, line)
				if (len(m.groups()) != 16 and log_reg == reg1) or (len(m.groups()) != 17 and log_reg == reg2):
					print '[error]' + line
				else:
					browser_type = m.groups()[9]
					if browser_type is None or browser_type == '':
						print line
					num = result.get(browser_type)
					if num is None:
						result[browser_type] = 1
					else:
						result[browser_type] = num + 1					
	finally:
		log.close()
		
def write_result_to_file(file_name):
	result_file = open(file_name, 'w')
	try:	
		for line in result:
			times = str(result.get(line))
			result_file.writelines(times + ',' + line + '\r')
	finally:
		result_file.flush()
		result_file.close()
    
if __name__ == '__main__':
	root = 'd:/opt/nginx_log/'
	file_name = 'd:/opt/browser.txt'
	traverse(root)
	write_result_to_file(file_name)
	result = ''
