# coding: utf-8
import xlwt
wb = xlwt.Workbook()
sh = wb.add_sheet("sheet1")
sh.write(1,1,"位置")

wb.save("测试.xls")


























'''
i = 0
aa = True
while aa:
	f = open('test.txt', 'r')
	a = f.readlines()[i:i+100]
	ff = open('10月{}-{}.txt'.format(i, i+100), 'a+')
	sep = ""
	ff.write(sep.join(a))
	i += 100
	if i >= 600:
		aa = False
'''


'''
f = open("11.txt", 'r')
a = f.read()
b = open('111.txt', 'a+')
i = 11
aa = True
while aa:
	b.write(a[i-11:i] + "\n")
	i += 11
	if i > len(a):
		aa = False
'''


'''


file = open('11.csv', 'r', encoding='utf-8')
a = file.read()
a = a.split(",")

for i in a:
	f = open('11.txt', "a+", encoding='utf-8')
	f.write(i)
'''