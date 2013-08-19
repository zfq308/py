import sys
import random

file = open('D:/data.txt', 'r')
new_file = open('D:/new_data.txt', 'w')
ip_file = open('D:/ip.txt', 'w')
for line in file:
    line = line.strip('\n')
    line = line.replace(" ", "")
    city, netbar_name, address, ip, cn_master  = line.split(',')
    if(ip == '' or ip is None):
        pass
    else :
        line = 'insert into t_s2_netbar (cn_master, ip, lvl) values (\'' + str(random.randint(0, 1000000)) + '\', INET_ATON(\'' + ip + '\'), 100);'
        ip_file.writelines( ip + '\n')
        new_file.writelines(line + '\n')
        new_file.writelines('commit;\n')
new_file.close()
ip_file.close()
file.close()
