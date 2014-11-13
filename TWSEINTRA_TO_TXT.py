# -*- coding: cp936 -*-
import os
import sys
import time
import shutil

oldFileType = '.TWSEINTRA'
newFileType = '.txt'

target = ''

def main():
    root = raw_input('请输入待处理的文件所在的路径：\n').strip()
    if (not os.path.exists(root)):
        print '待处理的文件存放目录(' + root + ')不存在，请重新配置！'
        return
    global target
    target = raw_input('请输入处理后文件的归档目录：\n').strip()
    if (os.path.exists(target)):
        print '处理后文件的归档目录(' + target + ')已存在，如果重要数据请保存，删除后重试！'
        return
    else:
        os.mkdir(target)
        print '处理后文件的归档目录(' + target + ")创建成功！"
        
    # 开始处理
    tree(root, '')


def tree(path, fileName):
    fullPath = path + os.sep + fileName
    if os.path.isfile(fullPath):
        if(fileName.endswith(oldFileType)):
            startPos = fileName.rfind('.TWSEINTRA')
            # 改文件类型
            newFileName = fileName[0:startPos] + newFileType
            newFillPath = target + os.sep + newFileName
            # 如果文件名相同，则改名：原名+时间+新的文件类型
            if (os.path.exists(newFillPath)):
                newFillPath = target + os.sep + fileName[0:startPos] + '_' + getTime() + newFileType
            # 拷贝到归档目录
            shutil.copy(fullPath, newFillPath)
            print fullPath + '\t' + newFillPath
    else:
        for temp in os.listdir(fullPath):
            tree(fullPath, temp)

def getTime():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


if __name__ == '__main__':
    main()
    print '处理完毕'
    os.system('Pause')
