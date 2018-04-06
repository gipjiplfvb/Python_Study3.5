#import re
#print(re.match('www', 'www.runoob.com').span())
#print(re.match('com', 'www.runoob.com'))
'''
i = 1
result = 1
while i<= 100:
	result = result * i
	i += 1

print (result)'''
'''
def test(num):
	if num > 1:
		return 	num * test(num - 1)
	else:
		return 1
a = test(100)
print (a)

print("Hello, World")
f = open("test1.txt","w",encoding=)
'''
'''
name = input("请输入你的文件名：")
name_d = name[:-4]+"复制" + name[-4:]
print (name_d)'''
a = ["a", "b", "c", "d"]
b = [1, 2, 3, 4]
c = []
i = 0
for j in range(len(a)**2):
	c.append('%s%d'%(a[i], b[0]))
	b.remove(b[0])
	if b==[]:
		i += 1
		b = [1, 2, 3, 4]
print(c)

