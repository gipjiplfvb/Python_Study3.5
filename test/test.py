'''
def f(a):
	b = True
	while b:
		i = a
		i **= a
		if a == 0:
			b = False
		print("a:", a, "i:", i)
		a -= 1
f(5)

def a(n):
	return 1 if n < 3 else a(n-1) + a(n - 2)
b = a(5)
print(b)







'''





'''
def hlt(n, x, y, z):
	if n == 1:
		print(x, '--->', z)
	else:
		hlt(n - 1, x, z, y)
		hlt(1, x, y, z)
		hlt(n - 1 , y, x, z)
print(hlt(3, '左', '中', '右'))
'''
'''
#coding=gbk
import chardet

def main():
    """ """

    name = input("please enter:" )
    result = chardet.detect(name.encode("utf-8"))
    print(result)

if __name__ == "__main__":
    main()
'''
'''
def test(num):
    list = [] #定义列表，用于存储计算
    i = num -1#去除本身
    while i > 1:#去除1
        if num%i == 0: #判断是否有余数
            list.append(i)#将所以有的能整除它数加入列表
        i -= 1
    if len(list) == 0:#如果列表为空，就是表示除了1个它本身能整除
        print(num,end=" ")


def test2(star_num,and_num):
    j = star_num
    while j < and_num:
        test(j)
        j += 1

test2(2,10001)
print("")'''
'''a = []
for i in range(3, 101, 2):
	for j in range(2, 10):
		if i % j == 0:
			if i == 3 or i == 5 or i == 7:
				a.append(i)
			break
	else:
		a.append(i)
print(a)


'''
'''
def day(x):
	
	m = 1
	for i in range(x):
		n = (m+1)*2
		m=n
	return m
sum = day(10)
print(sum)
'''
'''import re

a = ['world_1001.log-main-20180325-0', 'world_1001.log-main-20180314-8', 'world_1001.log-main-20180317-0', 'world_1001.log-main-20180314-4', 'world_1001.log-main-20180316-0', 'world_1001.log-main-20180313-0', 'world_1001.log-error-20180321-0', 'world_1001.log-error-20180314-0', 'world_1001.log-main-20180314-13', 'world_1001.log-error-20180319-0', 'world_1001.log-main-20180324-0', 'world_1001.log-error-20180315-0', 'world_1001.log-error-20180324-0', 'world_1001.log-main-20180322-0', 'world_1001.log-main-20180318-0', 'world_1001.log-error-20180326-0', 'world_1001.log-main-20180315-19', 'world_1001.log-main-20180314-7', 'world_1001.log-main-20180314-0', 'world_1001.log-main-20180314-3', 'world_1001.log-error-20180322-0', 'world_1001.log-main-20180323-0', 'world_1001.log-main-20180320-0', 'world_1001.log-main-20180314-2', 'world_1001.log-main-20180319-0', 'world_1001.log-error-20180313-0', 'world_1001.log-main-20180326-0', 'world_1001.log-main-20180314-1', 'world_1001.log-main-20180314-5', 'world_1001.log-main-20180314-9', 'world_1001.log-main-20180314-6', 'world_1001.log-main-20180314-10', 'world_1001.log-main-20180315-0','world_1001.log-main-20180314-12', 'world_1001.log-error-20180323-0', 'world_1001.log-error-20180314-1', 'world_1001.log-main-20180314-17', 'world_1001.log-main-20180314-11', 'world_1001.log-main-20180314-18', 'world_1001.log-main-20180314-14', 'world_1001.log-main-20180321-0', 'world_1001.log-main-20180314-15', 'world_1001.log-main-20180314-16', 'world_1001.log-error-20180316-0', 'world_1001.log-error-20180320-0']

def test(*args):
	b = []
	for i in args:
		bb = re.search(r'\d{8}', i)
		b.append(bb.group())
	return b
a.sort(key = test)
print(a)'''


#'world_1001.log-main-20180314-4', 'world_1001.log-main-20180316-0', 'world_1001.log-main-20180313-0', 'world_1001.log-error-20180321-0', 'world_1001.log-error-20180314-0', 'world_1001.log-main-20180314-13', 'world_1001.log-error-20180319-0', 'world_1001.log-main-20180324-0', 'world_1001.log-error-20180315-0', 'world_1001.log-error-20180324-0', 'world_1001.log-main-20180322-0', 'world_1001.log-main-20180318-0', 'world_1001.log-error-20180326-0', 'world_1001.log-main-20180315-19', 'world_1001.log-main-20180314-7', 'world_1001.log-main-20180314-0', 'world_1001.log-main-20180314-3', 'world_1001.log-error-20180322-0', 'world_1001.log-main-20180323-0', 'world_1001.log-main-20180320-0', 'world_1001.log-main-20180314-2', 'world_1001.log-main-20180319-0', 'world_1001.log-error-20180313-0', 'world_1001.log-main-20180326-0', 'world_1001.log-main-20180314-1', 'world_1001.log-main-20180314-5', 'world_1001.log-main-20180314-9', 'world_1001.log-main-20180314-6', 'world_1001.log-main-20180314-10', 'world_1001.log-main-20180315-0','world_1001.log-main-20180314-12', 'world_1001.log-error-20180323-0', 'world_1001.log-error-20180314-1', 'world_1001.log-main-20180314-17', 'world_1001.log-main-20180314-11', 'world_1001.log-main-20180314-18', 'world_1001.log-main-20180314-14', 'world_1001.log-main-20180321-0', 'world_1001.log-main-20180314-15', 'world_1001.log-main-20180314-16', 'world_1001.log-error-20180316-0', 'world_1001.log-error-20180320-0']
#a = ["aa20180101","bbc20180102","aaa20180101","qq20180103","dd20180101"]
#key = lambda x:(x[-8:])
#def xx(x):
#	return x[-8:]

#print(xx)
#a.sort(key = xx)
#print(a)


#key = lambda x:(re.search("\d{8}",x[x for i in a])


