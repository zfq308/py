#!/usr/bin/python
# encoding: utf-8

import sys
import os
import shutil



def getargs(list):
	arglist = ""
	for arg in list:
		if arg.find('-Xmx1024M') >= 0:
			arglist += ' -Xmx2048M'
		else:
                        if arg.find(':') >= 0:
                                if arg.find('=') >= 0:
                                        arg = arg[:arg.find('=')+1] + '"' + arg[arg.find('=')+1:] + '"'
                                else:
                                        arg = '"' + arg + '"'
			arglist += ' ' + arg		
	return arglist

if __name__ == '__main__':
	exename = 'java_back.exe'
	#if os.path.exists(exename) and os.path.isfile(exename):
	arg = getargs(sys.argv[1:])
##	print "cmd:%s"%(exename +' '+ arg)
	os.system(exename +' '+ arg)
