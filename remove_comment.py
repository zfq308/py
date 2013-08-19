import os
import re

def traverse(path):
    if os.path.isfile(path):
        analysis(path)
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp)

def analysis(path):
    print path
    f = open(path, 'r+')
    s = ''
    try:     
        for line in f:
            s += line
        s = del_comment(s)
        f.seek(0, 0)
        f.truncate();
        f.write(s);
        f.flush();
    finally:
        f.close()

def del_comment(s):
    left = s.find('/*')
    while(left != -1):
        right = s.find('*/', left)
        temp = s[left:right+2]
        s = s.replace(temp, '')
        left = s.find('/*')
    return s
        

if __name__ == '__main__':
    root = 'D:/repo/workspaces/java/BillingAgency/src/cyou/mrd'
    traverse(root)
