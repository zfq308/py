import os
import thread
import time
import shutil
import time
import sys

rootPath = '/Users/spruce/Downloads/src'
logFile = '/Users/spruce/Downloads/log.txt'
errorFile = '/Users/spruce/Downloads/error.txt'
resultPath = '/Users/spruce/Downloads/result'

files = []
counter = 0

def tree(path):
    global counter
    if os.path.isfile(path):
        f = open(path, 'r')
        for line in f:
            counter += 1
        f.close()
    else:
        for temp in os.listdir(path):
            tree(path + os.sep + temp)

if __name__ == '__main__':
    path = sys.argv[1]
    tree(path)
    print str(counter)
