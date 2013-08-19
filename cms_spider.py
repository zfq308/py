import urllib
import httplib
import codecs
import re
import time
import os


def is_page_exist(web_domain, link):
    conn = httplib.HTTPConnection(web_domain)
    conn.request("GET", link)
    response = conn.getresponse()
    if response.status == 200:
        return True
    else:
        return False

def get_url(url, page_index):
    reg = r'(.*)(\..*)'
    m = re.search(reg, url)
    return m.group(1) + '_' + str(page_index) + m.group(2)

def get_html(link):
    filehandle = urllib.urlopen(link)
    html = ''
    for line in filehandle:
        html += line
    return html

def get_list(html, list_class):
    reg_list = '<ul\sclass="' + list_class + '">((.|[\r\n])*?)</ul>'
    m = re.search(reg_list, html)
    if m == None:
        print 'get_list error'
        return ''
    return m.group(0)

def get_month(timestr):
        format = '%m/%d %H:%M'
        t = time.strptime(timestr, format)
        return t.tm_mon
        
def get_data(html, year, month):
    list = []
    reg_link = r'<a href=(.+?)\starget=_blank>(<font.*?>)?(.+?)(</font>)?</a><span>\((.+?)\)</span><br>'
    for line in re.findall(reg_link, html):
            if get_month(line[4]) <= month:
                    pass
            else:
                    month = get_month(line[4])
                    year = year - 1
            list.append((line[0], line[2], str(year) + '/' + line[4]))
    return (list, year, month)

def write_to_file(list, result_file_name, type):
    rf = codecs.open(result_file_name, 'a', 'utf-8')
    for temp in list:
            rf.write('insert into t_trans_temp(title, href, insert_time, channel_id) values (\'')
            rf.write((temp[1].strip() + '\', \'' + temp[0].strip() + '\', \'' + temp[2].strip() + '\', ' + str(type) + ');\n').decode('gbk'))
            rf.flush()
    rf.close()

def clear_file(file_name):
        rf = codecs.open(file_name, 'w', 'utf-8')
        rf.write('')
        rf.flush()
        rf.close()

def get_exist_urls(web_domain, page, max_page_no):
    if not is_page_exist(web_domain, page):
        return []
    else:
        pages = [page]
        while max_page_no > 0:
            temp_url = get_url(page, max_page_no)
            if is_page_exist(web_domain, temp_url):
                pages.append(temp_url)
            max_page_no = max_page_no - 1
        return pages
            

if __name__ == '__main__':
    list = [ {'domain':'gy.cy.com', 'page':'http://gy.cy.com/s2010/hd/index.shtml', 'result_file_name':'e:/cms/jx-gy/gy.sql', 'type':762, 'list_class':'sub_cont'}
            ,{'domain':'jx.changyou.com', 'page':'http://jx.changyou.com/s2010/hd/index.shtml', 'result_file_name':'e:/cms/jx-gy/jx.sql', 'type':763, 'list_class':'newsList'}]
    for one in list:
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
            web_domain = one['domain']
            list_class = one['list_class']
            page = one['page']
            result_file_name = one['result_file_name']
            type = one['type']
            urls_list = get_exist_urls(web_domain, page, 15)
            clear_file(result_file_name)

            for temp in urls_list:
                print '[process]' + temp
                data_list, year, month = get_data(get_list(get_html(temp), list_class), year, month)
                write_to_file(data_list, result_file_name, type)
