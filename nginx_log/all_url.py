import os

file_name = 'log'
special_url = 'GET /yhmxActive/index.jsp'

def traverse(path):
    if os.path.isfile(path):
        analysis(path)
    else:
        for temp in os.listdir(path):
            traverse(path + os.sep + temp)

def analysis(path):
    if file_name in path:
        print path
        log_file = open(path, 'r')
        result_file = open('d:/yhmxActive.log', 'a')
        for line in log_file:
            if special_url in line:
                result_file.write(line)
        log_file.close()
        result_file.close()
    else:
        pass

if __name__ == '__main__':
    traverse('D:/opt/nginx_log')
