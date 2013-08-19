import sys
import urllib

def cn_to_cnmaster(cn):
    cnmaster = urllib.urlopen('http://activity.changyou.com/cn_to_cnmaster.jsp?cn=' + cn).read()
    cnmaster = cnmaster.strip('\n')
    cnmaster = cnmaster.replace(" ", "")
    cnmaster = cnmaster.replace("\n", "")
    cnmaster = cnmaster.replace("\r", "")
    return cnmaster


cn_file = open('D:/cn.txt', 'r')
cnmaster_file = open('D:/cn_master.txt', 'w')

last_cn, cn_master = '', ''
for line in cn_file:
    line = line.strip('\n').strip('\r')
    line = line.replace(" ", "")
    city, netbar_name, address, ip, cn  = line.split(',')
    
    if city == '' or city is None or netbar_name == '' or netbar_name is None or address == '' or address is None or cn == '' or cn is None:
        pass
    else:
        if(last_cn == cn):
            pass
        else:
            cn_master = cn_to_cnmaster(cn)
            last_cn = cn
        line = city + ',' + netbar_name + ',' + address + ',' + ip + ',' + cn_master
        if cn_master == 'null' or cn_master == None or cn_master == '':
            #print cn
            print city + ',' + netbar_name + ',' + address + ',' + ip + ',' + cn
        cnmaster_file.writelines(line + '\n')
    
cn_file.close()
cnmaster_file.close()    
