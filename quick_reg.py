import urllib
import os
import random

def getstr(n): 
	al=list('abcdefghijklmnopqrstuvwxyz') 
	st='' 
	for i in range(n): 
		index = random.randint(0, len(al)-1) 
		st = st + al[index] 
		del al[index] 
	return st + '@changyou.com'

def test():
	c = ()

if __name__ == '__main__':
        total = 1000
        index = 0
        while(index < total):
                mail = getstr(10)
                print mail
                index += 1
	
	#os.system('pause')
	
