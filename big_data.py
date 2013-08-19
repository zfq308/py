import os
import sys
import os
import time
import thread
def analysis(log_file, result_path, table_head, table_count, point):
    log_file = open(log_file, 'r')
    result_file = open(result_path + os.sep + table_head + str(point), 'w')
    try:
        index = 0
        for line in log_file:
            if line is None or line == '' or line == '\n':
                pass
            else:
                if abs(hash(line.split(',')[0]))%table_count == point:
                    index += 1
                    if index%100000 == 0:
                        print time.ctime() + '[thread' + str(point) + ']' + str(index) + '\n'               
                    result_file.writelines(line)
                    result_file.flush()
                else:
                    pass
        print '[thread' + str(point) + '] finish time:' + time.ctime() + ', total line:' + str(index)
    except Exception, e:
         print e        
    finally:
        result_file.close()
        log_file.close()
        thread.exit_thread()
def go(data_file, count):
    print 'start time ' + time.ctime()
    # analysis('d:/opt/tldata.2012-09-12.csv', 'd:/opt/result', 't_bigdate_', 10)
    for i in range(count):
        print 'thread-' + str(i) + 'start'
        thread.start_new_thread(analysis, (data_file, 'd:/opt/result', 't_bigdate_', count, i))

if __name__ == '__main__':
    try:
        #analysis('d:/opt/tldata.2012-09-12.csv', 'd:/opt/result', 't_bigdate_', 10, 1)
        # thread.start_new_thread(analysis, ('d:/opt/tldata.2012-09-12.csv', 'd:/opt/result', 't_bigdate_', 10, 1))
        go('d:/opt/tldata.2012-09-12.csv', 10)
    except Exception, e:
         print e   
    #finally:
        #os.system('pause')