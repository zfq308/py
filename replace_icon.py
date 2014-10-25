import os
import sys
import shutil

new_app_icon = './app_icon.png'

def tree(path, name):
    fullpath = path + name
    if(os.path.isfile(fullpath)):
        if(name == 'app_icon.png'):
            print fullpath
            os.remove(fullpath)
            shutil.copy(new_app_icon, fullpath)
    else:
        for file in os.listdir(fullpath):
            tree(fullpath + '/', file)
    
if __name__ == '__main__':
    root = './'
    for file in os.listdir(root):
        if (os.path.isfile(root + file) is False):
            tree(root, file)
