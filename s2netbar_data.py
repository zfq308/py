import sys

file = open('D:/origin.csv', 'r')
new_file = open('D:/new_data.txt', 'w')

for line in file:
    line=line.strip('\n')
    city, netbar_name, address, ips  = line.split(',')
    ip = ips.split('PPPP')
    for temp in ip:
        line = city + ',' + netbar_name + ',' + address + ',' + temp + '\n'
        print line
        new_file.writelines(line)
new_file.close()
file.close()
