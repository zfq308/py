import httplib
conn = httplib.HTTPConnection('10.127.64.209')
headers = {'Authorization':'Basic YWN0aXZpdHlsb2c6MjEzem8hIyUhQHhjdnVubDEzMms1'}
conn.request('GET','/background/logMonitor/shell.jsp?filepath=/opt/proxoolLog/&filename=proxoolinfo.log&num=5000',headers=headers)
result = conn.getresponse()
result.read()
