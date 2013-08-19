import sys
import os

def isBlankfolder(name):
	if(os.path.isdir(name)):
		if(len(os.listdir(name)) == 0):
			return True
		else:
			flag = True
			for subf in os.listdir(name):
				if(isBlankfolder(name + '\\' + subf) == False):
					flag = False
					break
			return flag
	else:
		return False

rs = open('d:\\rs.txt', 'w', -1, 'utf-8')
for file in os.listdir('d:\\logs\\activity'):
	temp = 'd:\\logs\\activity\\' + file
	if(isBlankfolder(temp) == True):
		print(temp)
		rs.write(temp + '\n')
rs.close()