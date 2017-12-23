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

print("测试", end=' ')
print("测试", end=' ')

print("测试", end=' ')
print("测试", end=' ')
print("测试", end=' ')


