'''f_name = input("请输入文件的名字：")
f = open (f_name,'w+')
print("请输入内容【单独输入“:w”保存退出】：")
datas = input("请输入你要保存的内容：")
while True:

	if datas == ":w" :
		break
	else:
		f.writelines("%s" % datas)
'''
'''
f = open("11.txt", 'r', encoding='utf-8')
g = open('22.txt', 'w+', encoding='utf8')
i = True
while i:
	a = f.readline()
	print (a)
	print("="*8)
	g.write('%s'%a)
	if len(a) == 0:
		i = False
g.close()
g = open('22.txt', 'r', encoding='utf8')
b = g.read()
print(b)


'''
'''def add_end(L=[]):
    L.append('END')
    return L
a = add_end()
print(add_end())
a = add_end()
print(a)
#####################################
'''




'''
for i1 in range(97, 123): # a-z
	for i2 in range(97, 123):
		for i3 in range(97, 123):
			for i4 in range(97, 123):
				for i5 in range(97, 123):
					a = open('33.txt', "a+", encoding='utf-8')
					code = chr(i1) + chr(i2) + chr(i3) + chr(i4) + chr(i5)
					a.write("%s\n"%code)
'''

a = ["1", "2", "3", "4", "5"]
b = []
for i1 in a:
	for i2 in a:
		for i3 in a:
			for i4 in a:
				for i5 in a:
					if i1 != i2 and i1 != i3 and i1 != i4 and i1 != i5 and i2 != i3 and i2 != i4 and i2 != i5 and i3 != i4 and i3 != i5 and i4 != i5:
						test = i1 + i2 + i3 + i4 + i5
						b.append(test)
print(b)
print(len(b))
