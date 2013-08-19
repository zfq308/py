#! /usr/bin/env python
#coding=utf-8
import os
import shutil
def get_num_of_string(folder_name):
    # online_20110627_15
    if folder_name == '' or folder_name is None:
        pass
    else:
        pieces = folder_name.split('_')
        return int(pieces[1] + pieces[2])

if __name__ == '__main__':
    folder_num_list = []
    for file in os.listdir('E:/release_new'):
        folder_num_list.append( get_num_of_string(file))
    folder_num_list.sort()
    for temp_folder in folder_num_list:
        folder_name = 'E:\\release_new\\' + 'online' + '_' + str(temp_folder)[0:8] + '_' + str(temp_folder)[8:10]
        new_folder_name = 'E:\\activity'
        print temp_folder
        os.system('Xcopy ' + folder_name + ' ' + new_folder_name + ' /ER /y')

         