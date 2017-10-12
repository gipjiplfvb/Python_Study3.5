#---coding = utf-8
import random
n = 0
while n < 4:
	n += 1
	x = 4 - n
	computer = random.randint(0, 2)
	print (computer)
	# 输入猜拳代表的数字
	guess = int(input("请输入你要猜的数字（0：拳头 1：布 2：剪刀):"))
	if guess >= 3:
		print ("输入的数字要小于3")
		n = 0
		continue
		# 不加continu的话输入数字大于3 就会直接执行下面的语句。
	if (guess == 0 and computer == 2) or (guess == 1 and computer == 0) or (guess == 2 and computer == 1):
		print ("你真牛B，赢了，奖励共享女友一个。")
		break
	elif guess == computer:
		print ("平局，来来来决战到天亮,你还有%d次机会。"%x)
		if x == 0:
			print ("次数用尽，bey")
	else:
		print ("哈哈，去洗洗手再来吧，你输了,你还在%d次机会"%x)
		if x == 0:
			print ("次数用尽，bey")

