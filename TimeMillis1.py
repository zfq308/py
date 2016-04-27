import time
import os

if __name__ == '__main__':
    time_str = raw_input('Enter Date(yyyy-mm-dd hh:mm:ss):\n')
    if time_str is None or time_str.strip() is '':
        print '--now--'
        print int(time.time() * 1000)
        print '----'
    else:
        print os.linesep
        print '--{}--'.format(time_str)
        print repr(int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')) * 1000))
        print '----'
