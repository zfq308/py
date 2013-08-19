import sys
import os

def printsubfolder(path, name, level):
    o = ''
    if(os.path.isfile(path + name)):
        for index in range(level - 1):
            o = o + '    '
        o = o + '|---'
        print(o + name + '\n')
    else:
        for index in range(level - 1):
            o = o + '    '
        o = o + '|---'
        
        if(level == 0):
            print(path + '\n')
        else:
            print(o + name + '\n')
            
        for file in os.listdir(path + name):
            printsubfolder(path + name + '\\', file, level + 1)
    
def tree(path):
    printsubfolder(path, '', 0)

tree('E:/release_new')