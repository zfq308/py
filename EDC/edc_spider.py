#!/usr/bin/env python
import urllib
import re
import os
import datetime
import time

IMG_PATH = 'e:/edc/'
DOWNLOAD_PROGRESS_TIMELINE_FILE = IMG_PATH + 'progress_timeline.txt'
DOWNLOAD_PROGRESS_IMAGE_URL_FILE = IMG_PATH + 'progress_image_url.txt'

# read a page
def GetHtml(link):
    filehandle = urllib.urlopen(link)
    html = ''
    for line in filehandle:
        html += line
    return html

# get timeline from page
def GetTimeline(html):
    reg_list = r'<a\sid="next_page_link"\shref="/archive\?before_time=(\d*)">'
    m = re.search(reg_list, html)
    return m.group(1)

def GetDetailPageUrl(html):
    url_reg = r'<a\starget="_blank"\sclass="hover"(?:\s|.)*?href="(.+?)">'
    p = re.compile(url_reg)
    return p.findall(html)

# Get image's url which we want 
def GetImageUrl(html):
    imageUrlRe = r'<img\ssrc="(.*?)"\sdata-highres="(.*?)"'
    m = re.search(imageUrlRe, html)
    url = m.group(2)
    if url == None:
        url = m.group(1)
    return url

# Get image file name
def GetImageName(url):
    imageNameRe = r'(.*?/)*(.*)'
    m = re.search(imageNameRe, url)
    return m.group(2)

def Download(img_url, img_name):
    img = open(IMG_PATH + img_name, 'wb')
    content = urllib.urlopen(img_url)
    for line in content:
        img.write(line)
    img.close()
    content = None

def SaveProgress(site, filename):
    try:
        img_file = open(filename, 'a')
        img_file.writelines(site + os.linesep)
    finally:
        img_file.close()

if __name__ == '__main__':
    print 'Start At ' + str(datetime.datetime.now())

    print '[Timeline Finshed]'
    f1 = open(DOWNLOAD_PROGRESS_TIMELINE_FILE, 'r')
    timelineList = []
    for line in f1:
        if line in timelineList:
            pass
        else:
            timelineList.append(line.strip(os.linesep))
            print line
    f1.close()
    
    print '[Image Url Finshed]'
    f2 = open(DOWNLOAD_PROGRESS_IMAGE_URL_FILE, 'r')
    imageUrlList = []
    for line in f2:
        if line in imageUrlList:
            pass
        else:
            imageUrlList.append(line.strip(os.linesep))
            print line
    f2.close()


    counter = 0;

    site = 'http://everyday-carry.com/archive'
    print '[Site]' + os.linesep + site

    try:
        while True:
            print '[Timeline]' + site

            html = GetHtml(site)
            if site not in timelineList:
                detailPageUrls = GetDetailPageUrl(html)
                for detailPageUrl in detailPageUrls:
                    print '---->' + detailPageUrl
                    try:
                        imageUrl = GetImageUrl(GetHtml(detailPageUrl))
                        if imageUrl in imageUrlList:
                            continue
                        imageName = GetImageName(imageUrl)
                        Download(imageUrl, str(time.time()) + '_' + imageName)
                        SaveProgress(imageUrl, DOWNLOAD_PROGRESS_IMAGE_URL_FILE)
                        counter += 1
                        print 'Download Counter ' + str(counter)
                    except Exception, e:
                        print e
            else:
                print 'pass'

            timeline = GetTimeline(html)
            site = 'http://everyday-carry.com/archive?before_time=' + timeline
            SaveProgress(site, DOWNLOAD_PROGRESS_TIMELINE_FILE)

    except Exception, e:
        print e
        print '[error]' + site

    print 'End At ' + str(datetime.datetime.now())
