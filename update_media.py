import os
import sys
import shutil

del_list = [
    ]
update_list = [
    'Plugin.jar'
    ]

src = 'Android_cyou'
target_list = [
    'Android_91',
    'Android_17173',
    'Android_18183',
    'Android_anfeng',
    'Android_baidumedia',
    'Android_cyouplus',
    'CPS_DuoWan',
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
    'CPS_ZhuoYi',
    'CPS_DuoMeng_CPA',
    'CPS_DuoMeng_CPC',
    'CPS_AiDeSiQi_CPA',
    'CPS_AiDeSiQi_CPC',
    'CPS_LiMei_CPA',
    'CPS_LiMei_CPC',
    'CPS_DianRu_CPA',
    'CPS_Inmobi',
    'CPS_Adwords',
    'CPS_ShouJiSOHU',
    'CPS_SOHU1',
    'CPS_AiDeSiQiWangYuYan_CPC',
    'CPS_DuoMengWangYuYan_CPC',
    'CPS_LiMeiWangYuYan_CPC',
    'CPS_YouLeYuan',
    'CPS_SanXing',
    'CPS_FanRen',
    'CPS_HangZhouSaiZhong',
    'CPS_KuWan'
    ]

root = 'f:/repo/mtlbb/MLDJ/BuildTool/Android/AndroidPlugins'

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

def update_config():
    config = open('config.properties', 'a')
    config.write('\n')
    config.write('GONGGAO_CHANNEL=http://baidu.com')
    config.write('\n')
    config.write('GONGGAO_COMMON=http://google.com')
    config.close()
    
if __name__ == '__main__':
    src = root + os.sep + src
    for target in target_list:
        channel = root + os.sep + target
        delete(channel)
        update(channel)
        os.chdir(channel + '/' + 'assets')
        update_config()
##        os.system('patch -p0 < ../../../patch')
##        os.system('patch ' + channel + '/AndroidManifest.xml patch')
