# encoding:utf-8
import os
import sys
import shutil

stockFilePath = ''

dataStock = {}

def cleanBlank(arr):
	newArr = []
	for i in arr:
		if i == '' or i == os.sep or i == '\r\n':
			continue
		else:
			newArr.append(i)
	return newArr

def save(stockNo, content):
	path = stockFilePath + os.sep + stockNo + '.txt'
	stockFile = open(path, 'a+')
	stockFile.write(content)
	stockFile.close()

def deleteStockFilePath():
	if os.path.exists(stockFilePath):
		shutil.rmtree(stockFilePath)
	os.mkdir(stockFilePath)

def error(filename, content):
	print filename + ',' + content

# sort function unimplement
def sort():
	stockKeys = dataStock.viewkeys()
	for stockKey in stockKeys:
		stock = dataStock[stockKey]
		dateKeys = stock.viewkeys()
		listKeys = list(dateKeys)
		listKeys.sort()
		content = ''
		for key in listKeys:
			lines = stock[key]
			for line in lines:
				content += line + '\r\n'
		save(stockKey, content)

def do(file):
	f = open(file, 'r')
	for line in f:
		if len(line) < 10:
			error(file, line)
		else:
			arr = cleanBlank(line.split(' '))
			if len(arr) != 17:
				error(file, line)
			else:
				stockNo = str(arr[1])
				stockDate = int(arr[0])
				stock = dataStock.get(stockNo)
				if stock is None:
					stock = {}
				oneDay = stock.get(stockDate)
				if oneDay is None:
					oneDay = []
				oneDay.append(line)
				stock[stockDate] = oneDay
				dataStock[stockNo] = stock
			
def tree(path):
	if os.path.isfile(path):
		do(path)
	else:
		for temp in os.listdir(path):
			tree(path + os.sep + temp)

def process(path):
	print 'process:' + path
	print 'delete:' + stockFilePath
	deleteStockFilePath()
	tree(path)
	sort()

if __name__ == '__main__':
	print 'start...'
	args = sys.argv[1:]
	if len(args) < 1:
		print 'Not input root path!'
		exit(0)
	root = str(args[0])
	stockFilePath = str(args[1])
	process(root)
	#print dataStock
	