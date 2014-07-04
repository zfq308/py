import sys
import os

def delFile(path):
    os.remove(path)

def printsubfolder(path, name, level, func):
    o = ''
    if(os.path.isfile(path + name)):
        for index in range(level - 1):
            o = o + '    '
        o = o + '|---'
        print(o + name + '\n')
        if name.endswith('.meta'):
            func(path + name)
        
    else:
        for index in range(level - 1):
            o = o + '    '
        o = o + '|---'
        
        if(level == 0):
            print(path + '\n')
        else:
            print(o + name + '\n')
            
        for file in os.listdir(path + name):
            printsubfolder(path + name + '\\', file, level + 1, func)
    
def tree(path):
    printsubfolder(path, '', 0, delFile)

tree('.')
