import time
import os

if __name__ == '__main__':
    time_str = raw_input('Enter Date(yyyy-mm-dd hh:mm:ss):\n')
    print repr(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')) * 1000)
