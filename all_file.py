import os
import shutil
import sys

rootPath = 'E:/Newfolder2'
logFile = 'E:/all_file.txt'
# rootPath = '/Users/spruce/Downloads/src'
# logFile = '/Users/spruce/Downloads/all_file.txt'

files = []

def tree(path):
    global counter
    if os.path.isfile(path):
        files.append(path)
    else:
        for temp in os.listdir(path):
            tree(path + os.sep + temp)

if __name__ == '__main__':
    tree(rootPath)
    log = open(logFile, 'a')
    for file in files:
        log.write(file + '\r')
    log.close()
