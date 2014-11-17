import os
import sys
import shutil

del_list = ['utdid.jar']
update_list = [
    'MobileSecSdk.jar',
    'Plugin.jar',
    'alipaysdk.jar',
    'assets/channel.properties',
    'core.jar',
    'res/drawable-hdpi/mgp_payment_way_alipay.png',
    'res/drawable-hdpi/mgp_payment_way_alipay_new.png',
    'res/layout/mgp_payment_root.xml',
    'res/values/mgp_arrays.xml',
    'res/values/mgp_strings.xml',
    'res/values/mgp_styles.xml',
    'utdid4all-1.0.4.jar'
    ]

src = 'Android_cyou'
target_list = [
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
        os.chdir(channel)
        os.system('patch -p0 < ..\AndroidManifest.xml.patch')
