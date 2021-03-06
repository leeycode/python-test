# 计算π的值
from random import random
from math import sqrt
from time import clock
DARTS = pow(2,18)
hits = 0
clock()
for i in range(1,DARTS):
	x,y = random(),random()
	# 到圆点的距离
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits/DARTS)
print('Pi的值是 %s' % pi)
print('程序运行时间是 %-5ss' % clock())