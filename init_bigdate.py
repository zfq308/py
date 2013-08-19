import sys
import os
import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

def generate_file(file_name):
    log_file = open(file_name, 'w')
    # single file contains 10000000 line
    for index in range(10000000):
        cn_master = ''
        level = random.randint(0, 100)
        for i in range(10):
            cn_master += chars[random.randint(0, 35)]
        cn_master += '@changyou.com'
        line = cn_master + ',' + str(level) + '\n'
        log_file.writelines(line)
        if index%10000 == 0:
            print file_name + '--' + str(index)
    log_file.close()

if __name__ == '__main__':
    for index in range(10):
        print 'start ' + str(index)
        generate_file('D:/logs/bigdata/' + str(index) + '.log')
        print 'end ' + str(index)
        
        