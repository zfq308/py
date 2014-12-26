import os
import sys

FolderCY='D:/repo/MLDJClient/Version/Main/Project/Public/OtherTools/AndroidPlugin/anzhi/CYMGChannelCY/'
FolderThird='D:/repo/MLDJClient/Version/Main/Project/Public/OtherTools/AndroidPlugin/anzhi/CYMGChannelAnZhi/'
FolderProject='D:/repo/MLDJClient/Version/Main/Project/Public/OtherTools/AndroidPlugin/anzhi/MTLBB/'

def printsubfolder(root, path, name):
    if(os.path.isfile(path + name)):
        fileName = path + name
        fileName = fileName.replace(root, FolderProject)
        if os.path.exists(fileName):
            print fileName
            os.remove(fileName)
    else:
        for file in os.listdir(path + name):
            printsubfolder(root, path + name + '/', file)
    
def tree(root):
    print 'Project:' + root
    printsubfolder(root, root + '/assets', '')
    printsubfolder(root, root + '/libs', '')
    printsubfolder(root, root + '/res', '')

if __name__ == '__main__':
    tree(FolderCY)
    tree(FolderThird)
