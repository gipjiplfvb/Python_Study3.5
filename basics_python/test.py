#coding=utf-8
#score = int(raw_input("你得了多少分:"))
#if score >=60:
#    print '及格'
#else:
#   print '不及格'
#x = tom
#y = 121
#print type(x)
#print type(y)
#a = 50
#b = 50
#print a == b
#print a is b
#raw_input("1\ \nn\nPress the enter key to exit.")
#lang = "study python"
#print lang[0]
#print lang[3]
#print 'study python'[0]
#print lang.index('p')
#print lang
#b = lang [1:]
#print '这是b'
#print b
#c = lang[:10]
#print '这是c'
#print c
#d = lang[:]
#print '这是d\n',d
#print '这是d\n' + d
#print '这是d:\n%s' %d
#str1 = 'abcd'
#str2 = 'efgh'
#c = 'a' in str1
#print bool("a是不是在str1里面\n") + c  # 不知道为什么结果是"2"
#print type(c)
#print type("a是不是在str1里面\n")
#print str1 + str2
#print str1 + '- ->' + str2

#print "a是不是在str1里面\n" + str(c) #结果正常
#print "a是不是在str1里面\n" + str('a' in str1)  #结果正常
#print "a是不是在str1里面\n" , c
#s = 11
#print "I like %s"
#print "I like 8%E" %s
#print 'Suzhou is more than %d years. %s lives in here.' % (2500,"mahao")
#print "Today's temperature is %.2f" %1.145
#s1 = "I like {0}".format("python")
#print s1
#s = "2python" . isalpha()
#print s
#print type(s)
#a = s
#print "看看A等于多少",a
#print type(a)
#b = str(a)
#c = int(a)
#print b , c
#a = "I Love PYTHON"
#print a.split("o") ##去掉o
#b = " mahao "
#print b.strip()    #去掉两边的空格
#print b.lstrip()   #去掉左边的空格
#print b.rstrip()  #去掉右边的空格
#a = "Hello a World"
#print "把所有字母变成大写：\n" , a.upper()
#print "所有字母是不是都是大写：\n" , a.isupper()
#print "把所有字母变成小写：\n" , a.lower()
#print "所有字母是不是都是小写：\n" , a.islower()
#print "首字母变成大写：\n" , a.capitalize()
#print "首字母变成大写：\n" , a.title()
#print "所有首字母变是不是大写：\n" , a.istitle()
#c = "www.baidu.com"
#print c.split(".")
#b = c.split(".")
#print "用'.'把上面的列表拼接起来.\n",(".".join(b))
#print "用'*'把上面的列表拼接起来.\n",("*".join(b))
#name = '老齐'
#print name
#unicode_str = unicode('中文', encoding = 'utf-8')
#print unicode_str.encode('utf-8')
##import codecs
#codecs.open('office 2007sn.doc', encoding = 'utf-8')
#a = []  #定义一个变量a，它是list类型，并且是空的
#print type(a)   #用内置函数type()查看变量a的类型为"list"(列表)"
#print bool(a)    #bool()可看变量a的布尔值，因为是是空的所以显示False:
#bool()是一个布尔函数，作用是来判断一个对你是“真”或着“空”“假”。
#print a #打印list类型的变量a
#a = ['2',3,'mahao.foxmail.com']
#print a
#print type(a)
#print bool(a)
#url = "mahao.foxmail.com"
#print url[2]
#print url[:3]
#print url[4:9]
#lang = "mahao.foxmail.com"
#print lang[4:9]
#print a[0] ,a[1], a[1:], a[:2], a[2][1:9]
#lang = "python"
#print lang.index("y")
#lst = ['python', 'java', 'c++']
#print lst.index('java')
#print lang
#print lang[-1]
#print lst
#print lst[-1]
#print alst[::-1]
#alst = ['a', 'b', 'c']
#print alst[0:2]
#print alst[0:3]
#print alst[-3:]
#print list(reversed(alst))
#print list(reversed("12345456"))
#lst = ['python', 'java', 'c##']
#print len (lst)
#print alst + lst
#print alst * 3
#print lst * 3
#print 'a' in alst
#print 'pyth' in lst
#print max(lst), max(alst)
#print min(lst), min(alst)
#print cmp(lst, alst)
#alst[len(alst):]= [5]
#alst[3:] = ['xxoo']
#lst.append(7)
#alst.extend(lst)
#print lst
#astr = 'python'
#blst = [1, 3, 4, 5, 6, 5]
#print hasattr(alst, '__iter__')
#clst = [1,3]
#print hasattr(clst, '__iter__')
#print hasattr(4, '__iter__')
la = [1, 2, 3, 1, 1, 2, 2, 3, 1]
print (la.count(1))
#la.append('a')
#print la
#la.append('a')
#print la
#print la.count('b')
#all_users = ["ma", "gihub"]
#all_users.insert(0,"fuck")
#all_users.insert(4,"fuck")
#print len(all_users)
#all_users.remove('fuck')
#print len(all_users)
#print all_users
#all_users.pop(2)
#print all_users
#all_users.pop()
#print all_users
#a = [1, 2, 3, 4, 5, 2, 3]
#a.reverse()
#print a
#welcome_str = "welcome you"
#print welcome_str[0]
#print welcome_str[1]
#print welcome_str[len(welcome_str)-1]
#print welcome_str[4:]
#print welcome_str[::-1]
#a = " Python"
#b = a*3
#print (a*3).split()
#git_list = ["mac", "git", "io", "java"]
#print git_list[0]
#print git_list[len(git_list)-1]
#print git_list[0:2]*2
#b = ["Python"]
#print b*7
#first = "hello,world"
#print welcome_str
#print first + "," + welcome_str
#print welcome_str[1]
#print welcome_str[0] + "E" + welcome_str[2:]
#matrix = [[1, 2, 3], [4, 5, 6], 7, 8, 9]
#print matrix[1][2]
#line = "hello. I am ma. Welcome you."
#print line.split(".")
#print line.split("m")
#print line.split("m",1)
#s = "I am, Writing\npython\tbook on line"
#print s
#print s.split()
#print "".join(git_list)
#s = "abc"
#print s
#t = 123, 'abc', ["come", "here"], ('python', 'learn')
#print t
#print len(t)
#print type(t)
#print t[0]
#print type(t[0]), type(t[1]), type(t[2]), type(t[3])
#tls = list(t)
#print tls
#t_tuple = tuple(tls)
#print t_tuple
#citys = ["suzhou", "shanxi", "shanghai", "beijing"]
#citys_codes = ["0512", "029", "012", "010"]
#print "{} : {}" .format(citys[0], citys_codes[0])
#suzhou_code = 0512
#print suzhou_code
#print type(suzhou_code)
#mydict = {}
#print mydict
#person = {"name" : "qiwsir", "site" : "qiwsir.qithub.io", "language" : "python"}
#print person
#print type(person)
#print id(person)
#person["name1"] = "mahao"
#print person
#print id(person)
#name = (["first", "Google"] , ["second", "Yahoo"])
#print dict(name)
#ad = {}
#print id(ad)
#print type(ad)
#ad["name"] = "mac"
#print ad
#print id(ad)
#name = (["first", "Google"], ["second", "Yahoo"])
#print name
#wesite = dict(name)
#print wesite
#ad = dict(name = "mac", age = 42)
#print ad
#"""
#-*- coding=UTF-8 -*-
import random
answer = random.randint(1,100)
print ('-------hello,world-------')
temp =input('猜猜我心里想的数字:')
guess=int(temp)
while guess != answer:
    print (answer)
    if guess < answer:
        print ('小了，小了')
        guess = int(input('猜错了，再次输入吧：'))
    if guess > answer:
        print ('大了，大了')
        guess = int(input('猜错了，再次输入吧：'))
else:
    guess = answer
    print ('猜中了，但是没有奖励！游戏结束')
#website = {}.fromkeys(("third", "forth"), "facebook")
#print website
#a = {("a", "b"): 1}
#c = ("a", "b")
#print a
#print type(a)
#print c
#print type(c)
#city_code = {'suzhou': '0512', 'beijing': '010', 'shanghai': '012', 'tangshan': '0315'}
#print len(city_code)
#print city_code
#city_code['nanjing'] = '025'
#print city_code
#a = city_code['shanghai']
#print a
#del city_code['shanghai']
#print city_code
#print 'Suzhou is a beautiful city, its area code is %(suzhou)s' % city_code
#a = {"name": "mac", "lang": "python"}
#b = a
#print b, "这是B值"
#c = b.copy()
#print c, "这是C值 COPY"
#print id(b), "这是B值"
#print id(c), "这是C值"
#c["name"] = "macs.com"
#print c, "这是C值,更改后的C"
#print b, "这是B值"
#b["name"] = "baidu.com"
#print b, "这是B值更改后的B和A的关系 是="
#print a, "这是A值"
#print c, "这是C值"
#x = {"name": "mac", "lang": ['python', 'java', 'c']}
#y = x.copy()
#print y, id(x), id(y)
#y["lang"].remove('c')
#print y, id(y)
#print x
#y["name"] = 'Tom'
#print y
#print x
#import copy
#z = copy.deepcopy(x)
#print z, id(x["lang"]), id(z["lang"])
#x.clear()
#print x
#del x
#print a
#d = {'lang': 'python'}
#print d.get('lang')
#print d.get('name')

#dd_kv = dd.items()
#print dd_kv, type(dd_kv)
#dd_iter = dd.iteritems()
#print dd_iter
#print list(dd_iter)
#print dd.keys()
#print dd.iterkeys()
#print list(dd.iterkeys())
#dd = {"name": "qiwsit", "lang": "python", "web": "www.baidu.com"}
#print dd
#print dd.pop("fang","name")
#print dd
#print dd.popitem()
#print dd
#d1 = {"lang": "python"}
#d2 = {"song": "I dreamed a dream"}
#d1.update(d2)
#print d1
#d2.update([("name", "mac"), ("web", "tom.com")])
#print d2
#print d2.has_key("web")
#print "web" in d2
#s1 = set("macocs")
#print s1
#s2 = set([123, "google.com", "face", "book", "facebook", "book"])
#print s2
#print type(s2)
#s3 = set{"facebook", [1, 2, 'a'], {"name": "python", "lang": "English"}, 123}
#print s3
#a_set = {'a', 'i'}
#print type(a_set)
#a_set.add("qiwsir")
#print a_set
#b_set = set("python")
#print type(b_set)
#print b_set
#f_set = frozenset("qiwsir")
#print f_set
#a_set = set("github")
#print a_set
#a_set.add("python")
#print a_set
#print "b" in a_set
#print "a" in a_set
#a = set("pqns")
#b = set("qsir")
#print a
#print b
#print a == b
#print a != b
#print a < b
#print b < a #b是a的子集
#print b.issubset(a)  #或用这种方法，判断b是否是a的子集
#print a.issuperset(a)   #判断a是否是c的超集
#print a | b
#print a.union(b)
#print b.union(a)
#print a & b
#print a.intersection(b)
#print a - b
#print b - a
#print a.difference(b)   #A相对B的差（补），即A相对B不同的部分元素
#print b.difference(a)
#print a.symmetric_difference(b)   #对称差集（去除相的部分，再合一起）
#a = 10.0
#b = 20.0
#print a > b
#print a < b
#print a == b
#print a != b
#print a - b
#print a + b
#print a * b
#print a / b
#for i in [1, 2, 3, 4, 5]:
#	print i,
#print "fuck\n" "tp,"
#import math
#print math.pow(3, 2)
#from math import pow
#print pow(3, 2)
#print (3, 2)
#from math import pow as pingfang
#print int(pingfang(4,98))
#import math
#print math.e
#x, y, z = 1, "python", ["hello", "world"]
#print x
#print y
#print z
#a = "itdiffer.com", "python"
#print a
#print type(a[0])
#print type(y)
#a = 10
#b = 20
#print a
#print b
#a, b = b, a
#print a
#print b
#tomp = a
#a = b
#b = tomp
#print a
#print b
#print tomp
#a = "I use python"
#b = "I use python"
#print a is b
#print id(b)
#print id(a)
#print a == b
#a = 8
#if a == 8:
#	print a
#print "请输入任意一个整数数字："
#number = int(raw_input())
#if number == 10:
#	print "你输入的数字是： %d" %number
#	print "You are SMRAT."
#elif number < 10:
#	print "你输入的数字是： %d" %number
#	print "This number is less than 10."
#elif number > 10:
#	print "你输入的数字是： %d" %number
#	print "This number is more than 10."
#else:
#	print "Are you a human?"
#name = "mac"  if "laoqi" else "github"
#print name
#name = "mac" if "" else "github"
#print name
#x = 2
#y = 8
#a = "python" if x > y else "qiwsir"
#print a
#b = "python" if x < y else "mac"
#print b
#hello = "world"
#for i in hello:
#	print i,
#for i in range(len(hello) - 1):
#	print hello [i],
#ls_line = ['hello', 'I am qiwsir', 'Welcome you', '']
#for world in ls_line:
#	print world
#for i in range(len(ls_line)):
##	print ls_line[i]
#print range(9)
#print range(0,29,3)
#print range(1,100,2)
#pythoner = ['I', 'am', 'a', 'pythoner', 'I', 'am', 'learning', 'it', 'with', 'qiwsir']
#py_index = range(len(pythoner))
#print py_index
#print range(0, 100, 3)
#aliquot = []
#for n in range(1, 100):
#	if n % 3 == 0:
#		aliquot.append(n)
#print aliquot
#name_str = "mahao"
#for i in name_str:
#	print i,
#name_list = list(name_str)
#print name_list
#for i in name_list:
#	print i,
#name_set = set(name_str)
#for i in name_set:
#	print i,
#name_tuple = tuple(name_str)
#for i in name_tuple:
#	print i,
#name_dict = {"name": "mahao", "lang": "python", "website": "mahao.github.io"}
#print name_dict
#for i in name_dict:
#	print name_dict[i]
#a = [1, 2, 3, 4, 5]
#b = [9, 8, 7, 6, 5]
#c = []
#for i in range(len(a)):
#	c.append(a[i] + b[i])
#print c
#print name_dict['name']
#a = [1, 2, 3, 4, 5]
#b = [9, 8, 7, 6, 5]
#print zip(a, b)
#print zip(a + b)
#elp(dict)
#m = {"name", "lang"}
#print type(m)
#a = "qiwsir"
#b = "github"
#print zip(a,b)
#m = 1
#x = range(1, 10)
#print x
#m *= 6
#print m

#m = 1
#for i in range(1,10):
	#print m *= i
#age = 20
#if age >= 30:
#	print "your age is ", age
#	print "adult"
#else:
#	print "your age is ", age
#	print "teenage"
height = input("请输入你的身高：")
weight = input("请输入你的体重：")
BMI = weight / height ** 2
print "--------测试结果--------"
if BMI <= 18.5:
	print "过轻"
elif 18.5 < BMI <= 25:
	print "正常"
elif 25 < BMI <= 28:
	print "过重"
elif 28 <BMI <= 32:
	print "肥胖"
else:
	BMI > 32
	print "严重肥胖"


# -*- coding=UTF-8 -*-
#import random
#answer = random.randint(1,100)
#print ('-------hello,world-------')
#temp =input('猜猜我心里想的数字:')
#guess=float(temp)
#while guess != answer:
#    print (answer)
#    if guess < answer:
#        print ('小了，小了')
#        guess = float(input('猜错了，再次输入吧：'))
#    elif guess > answer:
#        print ('大了，大了')
#        guess = float(input('猜错了，再次输入吧：'))
#else:
#    guess = answer
#    print ('猜中了，但是没有奖励！游戏结束')
#a = [1, 2, 3, 4, 5]
#b = [9, 8, 7, 6, 5]
#c = []
#for x, y in zip(a, b):
#	c.append(x + y)
#print c
#d = []
#a = [1, 2, 3, 4, 5]
#b = ["python", "www.iddiffer.com", "qiwsir"]
#length = len(a) if len(a)<len(b) else len(b)
#print length
#for i in range(length):
#	d.append(str(a[i]) + ":" +b[i])
#print d
#result = [(2, 11), (4, 13), (6, 15),(8, 17)]
#print zip(*result)
#myinfor = {"name": "qiwsir", "site": "qiwsir.github.io", "lang": "python"}
#infor = {}
#for k, v in myinfor.items():
#	infor[v] = k
#print infor
#print myinfor.values()
#print myinfor.keys()
#for i in range(len(week)):
#	print week[i] + ' is ' + str(i)
#a = "s"
#b = "S"
#print id(a)
#print id(b)
#print a == b
#mylist = ["qiwsir", 703, "python"]
#print type(mylist)
#print mylist
#print list(enumerate(mylist))
#seasons = ["Spring", "Summer", "Fall", "Winter"]
#print list(enumerate(seasons)) #enumerate 列举  列举出列表seasons所有元素并且按序号排列
#print list(enumerate(seasons, start = 1))    #序号从1开始
#mylist = ["qiwsir", 708, "python"]
#print list(enumerate(mylist))  #列举的时候要转换成列表类型
#lst = "Do you love Canglaoshi? Canglaoshi is good teacher."
#print list(enumerate(lst))
#raw_lst = lst.split(" ")   #splis通过空格分割
#print raw_lst
#print list(enumerate(raw_lst))
#for i, string in enumerate(raw_lst):
#	if string == "Canglaoshi":
#		raw_lst[i] = "PHP"
#		print raw_lst
#for i, string in enumerate(raw_lst):
#	if "Canglaoshi" in string:
#		raw_lst[i] = "php"
#		print raw_lst
#
#power2 = []
#for i in range(1, 10):
#	power2.append(i**2)
#print power2
#squares = [x**2 for x in range(1, 10)]
#print squares
#coding=utf-8
#zhong = "中文"
#unicode_str = unicode(zhong, encoding='utf-8')
#print unicode_str.encode('utf-8')
#print "我真是大明星"
#import random
#i = 0
#while i < 4:
#	print '************************'
#	num = input("请您输入0到9任一个数字：")
#	xnum = random.randint(0, 9)
#	x = 3 - i
#	if num == xnum:
#		print '运气真好，您猜对了！'
#		break
#	elif num > xnum:
#		print '''您猜大了！\n哈哈，正确答案是：%s\n你还有%s次机会！'''%(xnum, x)
#	elif num < xnum:
#		print '''您猜小了！\n哈哈，正确答案是：%s\n你还有%s次机会！'''%(xnum, x)
#print '************************'

#i += 1
#import random

#number = random.randint(1,101)

#guess = 0

#while True:


#    num_input = raw_input("请随便输入1-100之间的数字:")
#    guess += 1
#    if not num_input.isdigit():
#        print "Please input integer."
#     elif int(num_input) < 0 or int(num_input) >= 100:
#        print "The number should be in 1 to 100."
#     else:
#         if number == int(num_input):
#            print "非常好,你太棒了.你只猜了%d次, 你就成功了." % guess
#            break
#         elif number > int(num_input):
#             print "你输入的数字太小了."
#       elif number < int(num_input):
#            print "你输入的数字太大了."
#       else:
#            print "There is something bad, I will not work"

#print "hello world"     #注意到 print 是一个函数
#print '''这是一段多行字符串。这是它的第一行。
#This is the second line.
#"What's your name?, I asked.
#He said "Bond, James Bond."
#'''     # 三引号中的内容会原样输出。
#下面是格式化的方法。.format 从其它信息中构建字条串。
#age = 20
#name = "Saroop"
#print "{0} was {1} years old when the worte this book.".format(name, age)       #在python中是从0开始计数的。
#print "Why is {0} playing with that python.".format(name)
#我们可以通过联立字条串来达到相同的效果。
#print name + ' is ' +str(age) + ' years old.'
#但是上面的方法 太丑陋了也容易出错，所以不常用 。用.format的方法，转换字符串的工作将由它来完成。而不需要特别注明。
#当使用.format 方法时，我们可直接改动文字面不必与变量打交道，反之亦然。
#同时还应该注意数字只是一个可选选项。所以你同时可以写成这样：
#age = 20
#name = 'Swaroop'
#print '{} was {} years old when he wrote this book.'.format(name, age)
#print 'Why is {} playing with that python.'.format(name)
#python中.format 所做的事情便是将每个参数值替代至格式所在的位置。这之中可以有更详细的格式，例如：
# 对浮点数'0.333' 保留小数点后三位
#print '{0:.3f}'.format(1.0/3) # .3f保留小数点后三位
#使用下划线填充文本，并保持文字处于中间位置
#print '{0:_^11}'.format('hello')     #中间对齐宽度为11
#print '{0:.3f}, {1:_^11}'.format(1.0/3, 'hello')
#基于关键词输出 'Swaroop wrote A Byte of Python'
#print '{name} wrote {book}'.format(name = 'Swaroop', book = 'A Byte of Python')
#多个print输出出来的结果总是处于一个新的段落，即独立的一行。为了防止打印出来的结果出现换行，我们可以用end指定其应以空白结尾：
#--------------***************此段开始用的python3.5***************---------------
#name = "AdD lovelace"
#print (name.title())    #字条串首个单词首字母大写
#print (name.upper())    #upper字符串全大写
#print (name.lower())    #字符串全小写。
#first_name = "ada"
#last_name = "lovelace"
#full_name = first_name + " " + last_name    #拼接字符串
#print (full_name)
#print ("Hello, " + full_name.title() + "!")

#print ("Python")
#print ("\tpython")  #要在字符串中加制表符，可使用字符组合\t
#print ("Languages:\nPython\nC\nJavaScript") #要在字符串中添加换行符，可使用字符组合\n
#print ("Languages:\n\tPython\n\tC\n\tJavaScript")   #可以在同一个字符串中同时包含制表符和换行符，字符串“\n\t”让python换到下一行开头添加一个制表符，后面的C和JavaScript也一样。
#a = 10
#b = 10.1
#print (a)
#print (type(a))
#print (b)
#print (type(b))
#c = int(b)
#print (c)
#print (type(c))
#import aiomysql
#print (hello aiomysl)
