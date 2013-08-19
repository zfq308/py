import sys
import os

def print_folder(path, result):
    result_file = open(result, 'w', -1, 'utf-8')
    if os.path.isfile(path):
        print('path %s is a file'.formate(path))
    else:
        for folder in os.listdir(path):
            result_file.write(folder)
    
#print_folder(sys.argv[1])
print_folder('D:\\logs\\activity', 'D:\T.TXT')