import os
import thread
import time
import shutil
import time
import random

rootPath = 'E:/Newfolder2'
logFile = 'E:/log.txt'
errorFile = 'E:/error.txt'
resultPath = 'E:/result_new'
allFile = 'D:/all_file_online.txt'
allFileSorted = 'E:/all_file_after_sort.txt'

##rootPath = '/Users/spruce/Downloads/src'
##logFile = '/Users/spruce/Downloads/log.txt'
##errorFile = '/Users/spruce/Downloads/error.txt'
##resultPath = '/Users/spruce/Downloads/result_new'
##allFile = '/Users/spruce/Downloads/all_file_online.txt'

files = []
filesName = []
counter = 0

def tree(path):
    if os.path.isfile(path):
        files.append(path)
        filesName.append(int(os.path.basename(path).split('.')[0].split('_')[1]))
    else:
        for temp in os.listdir(path):
            tree(path + os.sep + temp)

def sort():
    log('Start sort...')
    for i in range(len(filesName)):
        filei = filesName[i]
        for j in range(i+1, len(filesName)):
            filej = filesName[j]
            if filej < filei:
                filesName[i], filesName[j] = filesName[j], filesName[i]
                files[i], files[j] = files[j], files[i]
    log('Sort done...')

def insertion_sort():
    log('Start insertion_sort...')
    total = len(filesName)
    if len(filesName) == 1:
        return
    for i in xrange(1, len(filesName)):
        if i % 1000 == 0:
            log('Sort : ' + str(i) + '/' + str(total))
        temp = filesName[i]
        tempFile = files[i]
        j = i - 1
        while j >= 0 and temp < filesName[j]:
            filesName[j + 1] = filesName[j]
            files[j + 1] = files[j]
            j -= 1
        filesName[j + 1] = temp
        files[j + 1] = tempFile
    log('Sort done...')

def saveFileName():
    log = open(allFileSorted, 'a')
    for file in files:
        log.write(file + '\r')
    log.close()

def log(msg):
    msg = time.ctime() + '\t' + msg + '\r'
    print msg
    log = open(logFile, 'a')
    log.write(time.ctime() + '\t' + msg + '\r')
    log.close()

def error(msg):
    print msg
    log = open(errorFile, 'a')
    log.write(time.ctime() + '\t' + msg + '\r')
    log.close()

def cleanBlank(arr):
    newArr = []
    for i in arr:
        if i == '' or i == os.linesep or i == '\r\n' or i == '\t' or i == '\n':
            continue
        else:
            newArr.append(i)
    return newArr

def save(stockNo, content):
    path = resultPath + os.sep + stockNo + '.txt'
    stockFile = open(path, 'a+')
    stockFile.write(content)
    stockFile.close()

def do(file):
    #stockNo:lines
    temp = {}
    before = time.time()
    f = open(file, 'r')
    for line in f:
        if len(line) < 10:
            error(file, line)
        else:
            arr = cleanBlank(line.split(' '))
            if len(arr) != 17:
                print str(arr)
                log('error\t' + file + '\t' + line)
            else:
                stockNo = str(arr[1])
                content = temp.get(stockNo)
                if content is None:
                    content = ''
                content += line
                temp[stockNo] = content
    for key in temp:
        save(key, temp[key])
    global counter
    counter += 1
    end = time.time()
    msg =  str(counter) + '/' + str(len(files)) + ',' + file + ',' + str(end - before)
    log(msg)

def load():
    print 'load ' + allFile
    f = open(allFile, 'r')
    for l in f:
        for path in l.split('\r'):
            if path == '' or path == '\r':
                continue
            files.append(path)
            filesName.append(int(os.path.basename(path).split('.')[0].split('_')[1]))
    f.close()
    
def load1():
    print 'load ' + allFileSorted
    f = open(allFileSorted, 'r')
    for l in f:
        for path in l.split('\r'):
            if path == '' or path == '\r':
                continue
            files.append(path)
            filesName.append(int(os.path.basename(path).split('.')[0].split('_')[1]))
    f.close()

def main():
    log('Start...')
    # get all file, save to files
    # tree(rootPath)
    load1()
    log('Total file number : ' + str(len(files)))
    # sort files
##    insertion_sort()
##    for file in files:
##        log(file)
    if os.path.exists(resultPath):
        shutil.rmtree(resultPath)
    os.mkdir(resultPath)
    for file in files:
        do(file)

if __name__ == '__main__':
    main()
##    load()
##    insertion_sort()
##    saveFileName()
    


