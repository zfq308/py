import os
import sys
import shutil

del_list = [
    ]
update_list = [
    'Plugin.jar',
    'core.jar',
    'res/values/mgp_arrays.xml',
    'res/values/mgp_strings.xml'
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
    'CPS_BanMa',
    'CPS_CyouTY',
    'CPS_DiYiYingYong',
    'CPS_HeiYou',
    'CPS_HongYanXinXi',
    'CPS_htc2',
    'CPS_JunHai',
    'CPS_LiangZiTuiGuang',
    'CPS_LiTian',
    'CPS_LiuJianFang',
    'CPS_MoLiDuo',
    'CPS_MuMaYi',
    'CPS_Netease',
    'CPS_PiPa2',
    'CPS_PuTao',
    'CPS_QingNing',
    'CPS_QiXiaZi',
    'CPS_QuWang',
    'CPS_SOHU',
    'CPS_Tencent',
    'CPS_TianYiLian',
    'CPS_YaMaXun',
    'CPS_YangShiChuanMei',
    'CPS_YiGuo',
    'CPS_YouXiDuo',
    'CPS_YouXiTanZi',
    'CPS_YouYi',
    'CPS_YouYou',
    'CPS_ZhuoYi'
    ]

root = 'F:/mtlbb/Version/TY/Project/Client/AndroidPlugins'

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
        os.chdir(root)
##        os.system('patch -p0 < ../../manifest.patch')
##        os.system('patch ' + channel + '/AndroidManifest.xml patch')
