import operator
import random

MAXTRIES = 2
ops = {'+':operator.add, '-':operator.sub}

def doprob():
	op = random.choice('+-')
	num = [random.randint(0, 10) for i in range(2)]
	num.sort(reverse=True)
	ans = ops[op](*num)
	pr = '%d %s %d = '% (num[0], op, num[1])
	oops = 0
	while(True):
		try:
			if(int(input(pr)) == ans):
				print('correct')
				break
			if(oops == MAXTRIES):
				print('answer is %d'%(ans))
				break
			else:
				print('incorrect...please try again')
				oops += 1
		except BaseException:
			print('error')