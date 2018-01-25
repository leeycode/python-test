# python语言类型
	# type(x):返回x类型，适合于所有类型的判断

# 1.数字类型
# 1.1 pow(x,y)函数
	# pow(2,10)=1024
	# pow(2,15)=32768
	# 可以嵌套使用：pow(2,pow(2,15))

# 1.2 相关函数
	# int(1.5) = 1
	# float(4) = 4.0

# 2.字符串

# 2.1索引值
# greet ="hello"
# print(greet[1])
# x=5
# print(greet[x-2])
# print(greet[0:3])

# 2.2 len()函数能够返回一个字符串的长度
# print(len(greet))

# 2.3大多数数据类型都可以通过str()函数转换为字符串
# print(str(123))


# 输入一个月份数字，返回对应月份名称的缩写

# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = input('请输入月份数（1-12）：')
# pos=(int(n)-1)*3
# monthAbbrev=months[pos:pos+3]
# print('月份简写是'+monthAbbrev+'.')

# weeks='星期一星期二星期三星期四星期五星期六星期天'
# n = input('请输入星期（1-7）：')
# pos=(int(n)-1)*3
# week=weeks[pos:pos+3]
# print('星期是'+week+'.')


# 3.元组和列表(跟js数组使用类似)

# 4.random库是使用
from random import *

# 随机生成一个小数
# print(random())
# 随机生成1-10之间的小数
# print(uniform(1,10))
# 随机生成一个整数
# print(randint(1,10))
# 在列表中随机选择一个数
# ra=[0,1,2,3,4,5,6,7,8,9]
# print(choice(ra))
# 随机选取x个元素
# print(sample(ra,4))


#字典
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
 
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
# print(dict['one'])          # 输出键为'one' 的值
# print(dict[2] )             # 输出键为 2 的值
# print(tinydict )            # 输出完整的字典
# print(tinydict.keys())      # 输出所有键
# print(tinydict.values())    # 输出所有值


#集合set 集合（set）是一个无序不重复元素的序列。
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
# print(student)

# if('Rose' in student) :
#     print('Rose 在集合中')
# else :
#     print('Rose 不在集合中')

a = set('abracadabra')
b = set('alacazam')
print(a - b)     # a和b的差集
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素