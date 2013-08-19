#! /usr/bin/env python
#coding=utf-8
import os
import sys
import datetime

def traverse(path):
    if os.path.isfile(path):
        analysis(path)
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp)

def analysis(path):
    file_name = os.path.split(path)[1]
    if is_legal_log(file_name):
        file = open(path, 'r')
        try:
            for line in file:
                print line
        finally:
            file.close()

def is_legal_log(file_name):
    '''
    (1) file_name must start with 'host.access.log'
    (2) file must be today's or yesterday's log file
    '''
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    if file_name.startswith('host.access.log'):
        tail = os.path.splitext(file_name)[1][1:9]
        if tail == today.strftime('%Y%m%d') \
            or tail == yesterday.strftime('%Y%m%d'):
            return True

def get_data(line):
    '''return useful data from line'''
    return ''

def record(data):
    '''record data'''
    pass

def generate_result_file():
    pass

def send_result(result_file):
    pass

if __name__ == '__main__':
    traverse('d:/opt/log1/nginx_log/')
    is_legal_log('')