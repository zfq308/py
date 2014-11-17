import os
import sys
import shutil

target_list = [
    'Android_cyou',
    'Android_91',
    'Android_17173',
    'Android_18183',
    'Android_anfeng',
    'Android_baidumedia',
    'Android_cyouplus',
    'Android_duowan',
    'Android_htc',
    'Android_maoren',
    'Android_muzhiwan',
    'Android_pipa',
    'Android_sougou',
    'Android_weiwan',
    'Android_xiaopiwang',
    'Android_youxiyuan',
    'CPS_91game',
    'CPS_7881',
    'CPS_19196',
    'CPS_AGuo',
    'CPS_AoYouTianXia',
    'CPS_BaiYu',
    'CPS_DiYiYingYong',
    'CPS_JunHai',
    'CPS_LiangZiTuiGuang',
    'CPS_LiTian',
    'CPS_MoLiDuo',
    'CPS_MuMaYi',
    'CPS_PiPa2',
    'CPS_PuTao',
    'CPS_QingNing',
    'CPS_QiXiaZi',
    'CPS_SOHU',
    'CPS_TianYiLian',
    'CPS_YiGuo',
    'CPS_YouXiTanZi',
    'CPS_YouYi',
    'CPS_YouYou',
    'CPS_ZhuoYi'
    ]

root = 'D:/repo/MLDJClient/Version/Main/Project/Client/AndroidPlugins/'
ty = 'F:/mtlbb/Version/TY_20141113/Project/Client/AndroidPlugins/'

def copy(a, b):
    if(os.path.exists(b)):
        shutil.rmtree(b)
    shutil.copytree(a, b)


if __name__ == '__main__':
    for target in target_list:
        a = root + os.sep + target
        b = ty + os.sep + target
        copy(a, b)
