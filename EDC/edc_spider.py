#!/usr/bin/env python
import urllib
import re
import os

img_url_file = 'd:/repo/py/EDC/img_file.txt'
IMG_PATH = 'd:/edc/'

def get_has_download_list():
    f = open(img_url_file, 'r')
    l = []
    for line in f:
        if line in l:
            pass
        else:
            l.append(line)
    f.close()
    return l

def get_html(link):
    filehandle = urllib.urlopen(link)
    html = ''
    for line in filehandle:
        html += line
    return html

def download(img_url, img_name, id):
    img = open(IMG_PATH + id + '_' + img_name, 'wb')
    content = urllib.urlopen(img_url)
    print IMG_PATH + id + '_' + img_name
    for line in content:
        img.write(line)
    img.close()
    content = None
    
def get_img_name(url):
    reg = r'http://(.*?)/(.*)'
    m = re.search(reg, url)
    return m.group(2)

def get_id(url):
    reg = r'http://everyday-carry.com/post/(\d*)/.*?'
    m = re.search(reg, url)
    return m.group(1)

def get_img(html):
    reg = r'<img\sid="image"\sclass="fit_to_screen"\ssrc="(.*?)"/>'
    m = re.search(reg, html)
    return m.group(1)

def get_detail_url(html):
    url_reg = r'<a\sid="post.*?class="brick.*?href="(.+?)"\s>'
    p = re.compile(url_reg)
    return p.findall(html)
    
def get_timeline(html):
    reg_list = r'<a\sid="next_page_link"\shref="/archive\?before_time=(\d*)">'
    m = re.search(reg_list, html)
    return m.group(1)

def write_to_file(path, mode, content):
    try:
        img_file = open(img_url_file, 'w+')
        img_file.writelines(img + os.linesep)
    finally:
        img_file.close()

def clear_file(path):
    try:
        img_file = open(img_url_file, 'a')
        img_file.writelines(img + os.linesep)
    finally:
        img_file.close()

def clear_file():
    try:
        img_file = open(img_url_file, 'w')
        img_file.writelines('')
    finally:
        img_file.close()

if __name__ == '__main__':
    has_download_list = get_has_download_list()
    site = 'http://everyday-carry.com/archive'
    try:
        while True:
            print '[-->]' + site
            html = get_html(site)
            if site in has_download_list:
                detail_url_list = get_detail_url(html)
                for cur in detail_url_list:
                    try:
                        img_id = get_id(cur)
                        img_url = get_img(get_html('http://everyday-carry.com/image/' + img_id))
                        print get_img_name(img_url)
                        download(img_url, get_img_name(img_url), img_id)
                    except Exception, e:
                        print e
            else:
                print 'pass'
            site = 'http://everyday-carry.com/archive?before_time=' + str(get_timeline(html))
            write_to_file(site)
    except Exception, e:
        print e
        print '[error]' + site

