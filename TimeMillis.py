import time
import os

if __name__ == '__main__':
    createValue = input('Enter TimeMillis:\n')
    createValue = float(createValue)
    createValue /= 1000
    print 'Date String:'
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(createValue))
    os.system('pause')
