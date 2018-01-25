# str1 = input('请输入一个人名：')
# str2 = input('请输入一个国家：')
# print('世界那么大，{}想去{}看看。'.format(str1,str2))


# n = input('请输入整数N：')
# sum = 0
# for i in range(int(n)):
# 	sum += i+1
# print('1到N求和结果：',sum)

# 打印九九乘法表
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print('{}*{}={:2} '.format(j,i,j*i),end='')
# 	print('')

# 计算阶乘1+2!+...+10!
# sum,tmp = 0,1
# for i in range(1,11):
# 	tmp*=i
# 	sum+=tmp
# print('运算结果是：{}'.format(sum))

# n=1
# for i in range(5,0,-1):
# 	n = (n+1)<<1
# print(n)

# diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
# for x in range(0,5):
# 	for y in range(0,5):
# 		if not(x==y):
# 			print('{}{}'.format(diet[x],diet[y]))


# from turtle import *
# fillcolor('red')
# begin_fill()
# while True:
# 	forward(200)
# 	right(144)
# 	if abs(pos()) <1:
# 		break
# end_fill()

# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
# 	forward(200)
# 	left(170)
# 	if abs(pos()) < 1:
# 		break
# end_fill()
# done()

# import turtle
# import time
# turtle.speed('fastest')
# turtle.pensize(2)
# for x in range(100):
# 	turtle.forward(2*x)
# 	turtle.left(90)
# time.sleep(3)


# import turtle
# import time
# turtle.pensize(2)
# turtle.bgcolor('black')
# colors = ['red','yellow','purple','blue']
# turtle.tracer(False)
# for x in range(400):
# 	turtle.forward(2*x)
# 	turtle.color(colors[x%4])
# 	turtle.left(91)
# turtle.tracer(True)
# done()

# 求平均数
# num1 = input('输入第一个数')
# num2 = input('输入第二个数')
# avg_num = (float(num1)+float(num2)) / 2
# print('平均数是 %.2f' % avg_num)


# 温度转换程序
# val = input('请输入带温度表示符的温度值（列如：30C:')
# if val[-1] in ['C','c']:
# 	f = 1.8 * float(val[0:-1]) + 32
# 	print('转换后的温度为： %.2fF'%f)
# elif val[-1] in ['F','f']:
#     c = (float(val[0:-1] - 32)) / 1.8
#     print('转换后的温度为： %.2fC'%c)
# else:
# 	print('输入有误')

# 绘制小蛇
import turtle
def drawSnake(rad,angle,len,neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300,800,0,0)
	pythonsize = 30
	turtle.pencolor('blue')
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)

main()