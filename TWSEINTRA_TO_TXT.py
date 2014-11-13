# -*- coding: cp936 -*-
import os
import sys
import time
import shutil

oldFileType = '.TWSEINTRA'
newFileType = '.txt'

target = ''

def main():
    root = raw_input('�������������ļ����ڵ�·����\n').strip()
    if (not os.path.exists(root)):
        print '��������ļ����Ŀ¼(' + root + ')�����ڣ����������ã�'
        return
    global target
    target = raw_input('�����봦����ļ��Ĺ鵵Ŀ¼��\n').strip()
    if (os.path.exists(target)):
        print '������ļ��Ĺ鵵Ŀ¼(' + target + ')�Ѵ��ڣ������Ҫ�����뱣�棬ɾ�������ԣ�'
        return
    else:
        os.mkdir(target)
        print '������ļ��Ĺ鵵Ŀ¼(' + target + ")�����ɹ���"
        
    # ��ʼ����
    tree(root, '')


def tree(path, fileName):
    fullPath = path + os.sep + fileName
    if os.path.isfile(fullPath):
        if(fileName.endswith(oldFileType)):
            startPos = fileName.rfind('.TWSEINTRA')
            # ���ļ�����
            newFileName = fileName[0:startPos] + newFileType
            newFillPath = target + os.sep + newFileName
            # ����ļ�����ͬ���������ԭ��+ʱ��+�µ��ļ�����
            if (os.path.exists(newFillPath)):
                newFillPath = target + os.sep + fileName[0:startPos] + '_' + getTime() + newFileType
            # �������鵵Ŀ¼
            shutil.copy(fullPath, newFillPath)
            print fullPath + '\t' + newFillPath
    else:
        for temp in os.listdir(fullPath):
            tree(fullPath, temp)

def getTime():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


if __name__ == '__main__':
    main()
    print '�������'
    os.system('Pause')
