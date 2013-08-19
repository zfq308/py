import sys

file = open('D:/formate_data.csv', 'r')
new_file = open('D:/new_data.txt', 'w')
last_city, last_netbar_name, last_address, last_ip, last_cn_master =  '', '', '', '', ''
for line in file:
    line = line.strip('\n')
    line = line.replace(" ", "")
    city, netbar_name, address, ip, cn_master  = line.split(',')
    if(city == '' or city is None or netbar_name == '' or netbar_name is None or address == '' or address is None or cn_master == '' or last_cn_master is None):
        line = last_city + ',' + last_netbar_name + ',' + last_address + ',' + ip + ',' + last_cn_master
    else:
        last_city, last_netbar_name, last_address, last_ip, last_cn_master = city, netbar_name, address, ip, cn_master
    print line
    new_file.writelines(line + '\n')
new_file.close()
file.close()
