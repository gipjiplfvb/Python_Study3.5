i = 0
while i < 9:
	i += 1
	j = 1
	while j <= i:
		k = j * i
		print ("%d*%d=%2d  "%(j, i, k), end="")
		j += 1
	print ("")

'''
val = input("你现在的温度是多少？请输入：")
if val[-1] in ['C', 'c']:
	f = 1.8 * float(val[0:-1]) + 32
	print ("转换后的温度为：%.2fF"%f)
elif val[-1] in ['F', 'f']:
	c = (float(val[0:-1]) - 32) / 1.8
	print ("转换后的温度为：%.2fc"%c)
else:
	print ("输入有误")
'''

