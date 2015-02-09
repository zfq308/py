import os
import thread
import time
import shutil
import time

rootPath = 'D:/test'
logFile = 'D:/log.txt'
resultPath = 'D:/result'

files = []

def tree(path):
    if os.path.isfile(path):
        files.append(path)
    else:
        for temp in os.listdir(path):
            tree(path + os.sep + temp)

def sort():
    log('Start sort...')
    for i in range(len(files)):
        filei = os.path.basename(files[i]).split('.')[0].split('_')[1]
        for j in range(i+1, len(files)):
            filej = os.path.basename(files[j]).split('.')[0].split('_')[1]
            if filej < filei:
                files[i], files[j] = files[j], files[i]
    log('Sort done...')
    
def log(msg):
    print msg
    log = open(logFile, 'a')
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
                save(stockNo, line)
    end = time.time()
    print (end - before), file, before, end
    
def main():
    log('Start...')
    # get all file, save to files
    tree(rootPath)
    log('Total file number : ' + str(len(files)))
    # sort files
    sort()
    for file in files:
        log(file)
    if os.path.exists(resultPath):
        shutil.rmtree(resultPath)
    os.mkdir(resultPath)
    for file in files:
        do(file)

if __name__ == '__main__':
    main()
