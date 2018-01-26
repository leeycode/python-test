# 控制结构

# 空气质量提醒
def main():
	PM = eval(input('输入PM2.5:'))
	if PM > 75:
		print('Unhealthy. Be carefull!')
	if PM < 35:
		print('Good. go running!')
# main()

# 多分支结构 if elif else

#try...except 异常处理语句

import math
def Smain():
	try:
		a,b,c = input('please enter the coefficients(a,b,c):')
		discRoot = math.sqrt(b*b-4*a*c)
		root1 = (-b + discRoot) / (2*a)
		root2 = (-b + discRoot) / (2*a)
		print('\nthe solution are:',root1,root2)
	except ValueError:
		print('\nNo real roots')

# Smain()

# 找出三个数值中最大值
def Max():
	x1,x2,x3 = eval(input('输入三个值：'))
	print(max(x1,x2,x3))
# Max()

# 基本循环结构
# for
# words = ['cat','window','defensestrate']
# for w in words:
	# print(w,len(w))

# 计算平均数
# n = eval(input('你有多少个数？'))
# sum = 0.0
# for i in range(n):
# 	x = eval(input('输入数字 >>'))
# 	sum = sum + x
# print(sum/n)

# 无限循环
# i = 0
# while i <= 10:
# 	print(i)
# 	i = i + 1
	