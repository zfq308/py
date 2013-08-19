import sys

log_file = open('d://logs//tl_detail_log//detail.log.2012-09-07', 'r')
new_file = open('d://logs//tl_detail_log//detail.log.2012-09-07.txt', 'w')

for line in log_file:
    str = line.split(',')
    if(str[0].endswith('164')):
        new_file.writelines(str[2] + ',' + str[5] + '\n')
    else:
        pass

new_file.close()
log_file.close()