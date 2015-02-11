import os
import thread
import time
import shutil
import time
import random

DATA_SRC = 'E:/Newfolder2'
LOG_FILE = 'E:/log.txt'
ERROR_FILE = 'E:/error.txt'
RESULT_PATH = 'E:/result_new'
UNSORT_FILE_NAMES = 'D:/all_file_online.txt'
SORTED_FILE_NAMES = 'E:/all_file_after_sort.txt'

# DATA_SRC = '/Users/spruce/Downloads/src'
# LOG_FILE = '/Users/spruce/Downloads/log.txt'
# ERROR_FILE = '/Users/spruce/Downloads/error.txt'
# RESULT_PATH = '/Users/spruce/Downloads/result_new'
# UNSORT_FILE_NAMES = '/Users/spruce/Desktop/zzh/all_file_online.txt'
# SORTED_FILE_NAMES = '/Users/spruce/Downloads/all_file_after_sort.txt'

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
    log = open(SORTED_FILE_NAMES, 'a')
    for file in files:
        log.write(file + '\r')
    log.close()

def log(msg):
    msg = time.ctime() + '\t' + msg + '\r'
    print msg
    log = open(LOG_FILE, 'a')
    log.write(time.ctime() + '\t' + msg + '\r')
    log.close()

def error(msg):
    print msg
    log = open(ERROR_FILE, 'a')
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
    path = RESULT_PATH + os.sep + stockNo + '.txt'
    stockFile = open(path, 'a')
    stockFile.write(content)
    stockFile.close()

def do(file):
    #stockNo:lines
    temp = {}
    startTime = time.time()
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
    endStatis = time.time()
    for key in temp:
        save(key, temp[key])
    endSave = time.time()
    global counter
    counter += 1
    endTime = time.time()
    msg =  str(counter) + '/' + str(len(files)) + ',' + file \
        + ',' + str(endTime - startTime)
        + ',' + str(endStatis - startTime)
        + ',' + str(endSave - endStatis)
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
            # print os.path.basename(path).split('.')[0].split('_')[1]
    f.close()
    
def loadSortedFiles():
    print 'load ' + SORTED_FILE_NAMES
    f = open(SORTED_FILE_NAMES, 'r')
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
    # tree(DATA_SRC)
    loadSortedFiles()
    log('Total file number : ' + str(len(files)))
    if os.path.exists(RESULT_PATH):
        shutil.rmtree(RESULT_PATH)
    os.mkdir(RESULT_PATH)
    for file in files:
        do(file)

if __name__ == '__main__':
    main()
    # load()
    # insertion_sort()
    # saveFileName()
    


