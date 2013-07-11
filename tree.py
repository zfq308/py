# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:18:34 2012

@author: spruce
"""

import os

def tree(root):
    if os.path.isfile(root):
        print root
    else:
        for temp in os.listdir(root):
            tree(root + os.sep + temp)

if __name__ == '__main__':
    tree('/home/spruce')