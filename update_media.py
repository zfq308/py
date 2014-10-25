import os
import sys
import shutil

del_list = []
update_list = [
    'res/values/mgp_strings.xml',
    'core.jar',
    'Plugin.jar'
    ]

src = 'Android_cyou'
target_list = [
    'Android_91',
    'Android_17173',
    'Android_18183',
    'Android_anfeng',
    'Android_baidumedia',
    'Android_duowan',
    'Android_maoren',
    'Android_muzhiwan',
    'Android_pipa',
    'Android_sougou',
    'Android_weiwan',
    'Android_xiaopiwang',
    'Android_youxiyuan'
    ]

root = 'D:/repo/MLDJClient/Version/TY/Project/Client/AndroidPlugins/'

def delete(channel):
    for d in del_list:
        p = channel + os.sep + d
        if(os.path.exists(p)):
            os.remove(p)
            print '[D]' + p

def update(channel):
    for d in update_list:
        p = channel + os.sep + d
        if(os.path.exists(p)):
            os.remove(p)
            shutil.copy(src + os.sep + d, p)
            print '[U]' + p

if __name__ == '__main__':
    src = root + os.sep + src
    for target in target_list:
        channel = root + os.sep + target
        delete(channel)
        update(channel)
