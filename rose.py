#! /usr/bin/env python
#coding=utf-8
import os
import sys
import re
import tarfile
import time
import logging

def tree(root):
    if os.path.isfile(root):
        anlysis(root)
    elif os.path.isdir(root):
        for temp in os.listdir(root):
            if os.path.exists(root + os.sep + temp):
                tree(root + os.sep + temp)
    
def anlysis(file_path):
    if not is_this_day_log(file_path):
        return
    if is_audit_gzip(file_path):
        t = tarfile.open(file_path, "r:gz")
        try:
            for f in t:
                file_name = file_path + '-' + f.name
                logger.debug(file_name)
                logger.debug('[start unzip]' + time.ctime())
                data = t.extractfile(f)
                temp = data.readlines()
                logger.debug('[end unzip]' + time.ctime())
                try:
                    analysis_data(temp)
                except:
                    logger.exception('gzip analysis_data error!')
                    data.close()
                    temp = None
                    data = None
                    raise        
                else:
                    data.close()
                    temp = None
                    data = None
        finally:
            t.close()
    elif is_audit_log(file_path):
        logger.debug(file_path)
        data = open(file_path, 'r')
        try:        
            analysis_data(data)
        except:
            logger.exception('log analysis_data error!')
            data.close()
            data = None
            raise        
        else:
            data.close()
            data = None
    else:
        logger.debug('-->do not process[not gzip or log] : ' + file_path)

def analysis_data(data):
    logger.debug('[start anlysis]' + time.ctime())
    for line in data:
        if 'LUAAUDIT_2013_SEND_ROSE' in line:
            result_send.append(line)
        elif 'LUAAUDIT_2013_RECEIVE_ROSE' in line:
            result_receive.append(line)
    logger.debug('[end anlysis] ' + time.ctime())

def is_this_day_log(file_name):
    reg = '.*?Audit_' + log_time + '.*?'
    m = re.match(reg, file_name)
    return m is not None

def is_audit_gzip(file_name):
    reg = r'.*?Audit.*?\.tgz'
    m = re.match(reg, file_name)
    return m is not None

def is_audit_log(file_name):
    reg = r'.*?Audit.*?\.log'
    m = re.match(reg, file_name)
    return m is not None

def write_result_to_file(current_time):
    result_file = open(result_file_path, 'w')
    try:
        for t in result_send:
            result_file.writelines(t + os.linesep)
        for t in result_receive:
            result_file.writelines(t + os.linesep)
        result_file.writelines('[END]' + current_time)
    except:
        logger.exception('write_result_to_file error!')
        result_file.close()
        os.remove(result_file_path)
        raise    
    else:
        result_file.flush()
        result_file.close()

def init_logging(logging_file_name):
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(lineno)s]%(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    hdlr = logging.FileHandler(logging_file_name)
    hdlr.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(hdlr)
    logger.setLevel(LOGGING_LEVEL)
    return logger

    
if __name__ == '__main__':
    LOGGING_LEVEL = logging.DEBUG
    
    SEND_ROSE_TYPE = 0
    RECEIVE_ROSE_TYPE = 1
        
    ## result_send    : send rose result, format:{guid:(server_id, send_guid, send_name, num)}
    ## result_receive : receive rose result, format:{guid:(server_id, receive_guid, receive_name, total revice rose num)}    
    result_send, result_receive = [], []
    current_time = time.strftime('%Y%m%d_%H%M')
    
    if len(sys.argv) != 4:
        print 'Method of execute this script is Wrong!'
    else:
        if not os.path.isdir(sys.argv[2]):
            print 'Result file path Error!' + os.linesep\
                + sys.argv[2] + ' is not a dir!'
        else:
            log_root_path = sys.argv[1]
            result_file_path = sys.argv[2] + os.sep + 'audit_rose_' + current_time + '.log'
            logging_file_name = sys.argv[2] + os.sep + 'activity_rose_script_log.log'
            log_time = sys.argv[3]
            
            # logging initial
            logger = init_logging(logging_file_name)
            
            logger.info('root : ' + log_root_path)
            logger.info('result file location : ' + result_file_path)
            logger.info('log time : ' + log_time)
            logger.info('start : ' + time.ctime())
            try:
                # traverse log files, and process into result data
                tree(log_root_path)
                # write result data to a file
                write_result_to_file(current_time)                
            except:
                logger.exception('main error!')

            result_send, result_receive = None, None
            logger.info('end :' + time.ctime())