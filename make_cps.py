import os
import sys
from shutil import copytree, rmtree, ignore_patterns

##new_app_icon = './app_icon.png'
##
##def tree(path, name):
##    fullpath = path + name
##    if(os.path.isfile(fullpath)):
##        if(name == 'app_icon.png'):
##            print fullpath
##            os.remove(fullpath)
##            shutil.copy(new_app_icon, fullpath)
##    else:
##        for file in os.listdir(fullpath):
##            tree(fullpath + '/', file)
##    
##if __name__ == '__main__':
##    root = './'
##    for file in os.listdir(root):
##        if (os.path.isfile(root + file) is False):
##            tree(root, file)

root = '.'
template = 'Android_cyou'
template_cmbi_channel_id = '2010752002'
template_channel_string = 'ANDROID_CYOU'
template_umeng = 'Android_cyou'
cps = ['CPS_SOHU', 'CPS_BaiYu', 'CPS_YiGuo', 'CPS_TianYiLian', 'CPS_JunHai', 'CPS_PiPa2']
channel_id = 120

def makeCps(channel):
    print 'make:' + channel
    cps_path = root + os.sep + channel
    if os.path.exists(cps_path):
        rmtree(cps_path)
    copytree(root + os.sep + template, cps_path)

def replace(filePath, tag, value):
    pass

if __name__ == '__main__':
    print 'template:' + root + os.sep + template
    for channel in cps:
        makeCps(channel)
