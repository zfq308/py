import sys
import os

def clear(path, name):
    #print(path + '\\' + name)
    if(os.path.isfile(path + '\\' + name)):
        if((name).startswith('detail.log')):
            #print(path + '\\' + name)
            pass
        else:
            #pass
            print(path + '\\' + name)
            os.system("del " + path + '\\' + name)
    else:
        for file in os.listdir(path + '\\' + name):
            clear(path + '\\' + name, file)
            
clear('D:\\logs\\tl_detail_log', '')