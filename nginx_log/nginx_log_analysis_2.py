#! /usr/bin/env python
#coding=utf-8
import os

url = '/tlWeixin/jsp/dealLogin.jsp'
count = 0

# 遍历日志目录，并返回处理结果
def traverse(path):
    if os.path.isfile(path):
        analysis(path)
        print path
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp)

# 分析日志文件
def analysis(path):
    global count
    f = open(path, 'r')
    for line in f:
        if url in line:
            count += 1
    f.close()


if __name__ == '__main__':
    traverse('d:\\opt\\nginx_log')
    print count
    
