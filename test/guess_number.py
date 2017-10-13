'''import random
a = random.randint(1, 100)
b = int(input("请输入你想猜的数字："))
while a != b:
	if b == a:
		print ("没问题老铁！")
	else:
		if b>a:
			print ("大了")
		elif b<a:
			print ("小了")
print ("结束")'''
import random
a = random.randint(1,10)
b = int(input ("输入数字："))
print (a)
while a!=b:
	if a > b:
		print("小了")
		b = int(input("输入数字："))
	elif a < b:
		print("大了")
		b = int(input("输入数字："))
print ("没问题老铁")

'''import random
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
    print ('猜中了，但是没有奖励！游戏结束')'''


