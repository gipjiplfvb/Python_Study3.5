# -*- coding: utf-8 -*-
print ('包含中文的str')
# Python提供了ord()函数获取字符的整数表示。
print (ord("A"))
print (ord("中"))
# Python提供了chr()函数把编码转换为对应的字符。
print (chr(66))
print (chr(25991))
# 如果想知道字符的整数编码，还可以用16进制这么写str:
print ("\u4e2d\u6587")
# Python对bytes类型的数据用带b的前缀的单引号或双引号表示：
x = b'ABC'
print (x)
print (type(x))
# 注意区分‘ABC’和b‘ABC’，前者是‘str’类型，后者虽然内容显示得和前者一样，但byte的每个字符都上占有用一个字节
# 以Unicode表示str通过encode()方法可以编码为指定的bytes，例如：
print ('ABC'.encode('ascii'))
print ('中文'.encode('utf-8'))
#print ('中文'.encode('ascii')) 含有中文的str不能转为ascii因为超出了它他范围。
print ('Hello, %s' %'world')
print ('Hi, %s, you have $%d.' %('Michale', 100000))

s1 = 71
s2 = 85
s3 = (s2 - s1)*1.0
print ("小明去年的成绩是：%s,今年的成绩是：%s."%(s1, s2), "两次成绩的涨浮是：%s%%"%s3)
L = [
	['Apple', 'Google', "Microsoft"],
	['Jave', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
	]
print (L[0][0])
print (L[1][1])
print (L[2][2])
sum = 0
for x in range(99):
	x = x - 2
	sum = sum + x
print (sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print (sum)
L = ['Bart', 'Lisa', 'Adam']
for i in L:
	print ("Hello,", i, "!")
n = 1
while n <= 2:
	print (n)
	n = n + 1
print ('End')

hello = "world"
for i in range(len(hello)):
	print (hello[i])
	print (hello)
