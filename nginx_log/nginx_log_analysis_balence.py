#! /usr/bin/env python
#coding=utf-8
import os
import sys

def traverse(path):
    if os.path.isfile(path):
        analysis(path)
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp)

def analysis(path):
    print '[analysis]' + path
    file = open(path, 'r')
    try:
        for line in file:
            ips = belong_to(line)
            for ip in ips:
                if result.get(ip) is None:
                    result[ip] = 1
                else:
                    result[ip] = result[ip] + 1
    finally:
        file.close()

def belong_to(line):
    ips = []
    for ip in resin_ips:
        if ip in line:
            ips.append(ip)
    return ips
                               
if __name__ == '__main__':
    result = {}
    resin_ips = ['10.127.64.209', '10.127.64.224', '10.127.64.195',
                 '10.127.64.196', '10.127.64.203', '10.127.64.204',
                 '10.127.64.210', '10.11.154.96', '10.11.154.97', '10.11.55.25']
    traverse('d:/opt/nginx_log')
    for key in result:
        print key + ':' + str(result[key])
