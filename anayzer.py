import os

logRootPath = 'D:\\logs\\detail.log.2012-02-23'

def anayze(filePath):
    file = open(filePath, 'r', -1, 'UTF-8')
    counter = 0
    try:  
        for line in file:
            counter += 1
            print(line)
    except UnicodeDecodeError:      
        print('exception found')  
    finally:
        print('counter = %d', counter)
        file.close()
anayze(logRootPath)