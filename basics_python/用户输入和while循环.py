# coding=utf-8
# 函数input()工作原理：函数 input（）让程序暂停运行，等等用户输入一些文本。获取用户输入后，python将其存储在一个变量中，以方便你使用
#name = input("Please enter your name: ")
#print ("Hello, " + name + "!")
#prompt = "If you tell us who you are, we can #personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print ("\nHello, " + name + "!")

# 求模运算符
# 如果一个数可被另一个数整数余数就是0，因此求模运算将返回0.你可以利用这点来判断一个数是奇数还是偶数：
#number = input("Enter a number, and I'll tell you if it's even or odd:")
#number = int (number)
#if number % 2 == 0:
#print ("\nThe number " + str(number) + " is 'even'")
#else:
#	print ("\nThe number " + str(number) + " is 'odd'")
# while循环。
'''current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print (message)'''
# 使用标志：在要求很多条件都满足才能继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为“标志”，充当了程序的交通信号灯。你可以让程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行。这样在While语句中只需检查一个条件--标志的当前值是否为Ture，并将所有测试（是否发生了应将标志设置为False的事件）都放在其它地方，从而让程序变的更整洁。、
#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program."

#active = True
#while active:
#	message = input(prompt)
#	if message == 'quit':
#		active = False
#	else:
#		print (message)
# 使用break退出循环
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you rae finished.)"
#while True:
#	city = input(prompt)
#	if city == 'quit':
#		break
#	else:
#		print ("I'd love to go to " + city.title() + "!")
#current_number = 0
#while current_number < 10:
#	current_number += 1
#	if current_number % 2 == 0:
#		continue
#	print (current_number)
# 用while循环来处理列表和字典。
# 到目前为止，我们每次都只处理一项用户信息：获取用户输入，再将输入结果打印出来或作出应答；循环再次运行时，我们获悉另一个输入值并作为响应。然而需要记录大量的用户和信息，需要在while循环中使用列表和字典。
# for 循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致python难以跟踪其中的元素。要在遍历列表的同时对其修改，可使用while，通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。
'''unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print ("Verifiying user: " +current_user.title())
	confirmed_users.append(current_user)

print ("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
	print (confirmed_users.title())'''


#输入整数求合。
'''
print ("*******************************")
number_1 = []
while True:
	number = input("请输入你的数字：")
	if number == 'q':
		break
	elif number.isalpha():
		print ("你所输入的'{}'不是数字，请重新输入".format(number) )
	else:	#这行代码意思是number_1最后汇总的时候列表中没有q
		number_1.append(number)
print ("**下面是你录的数据***")
print (number_1)
numbers = [int(x) for x in number_1]
print (sum(numbers))
'''
responses = {}
polling_actve = True
while polling_actve:
	# 提示输入被调查的名字和回答
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb somday? ")
	# 将答案在字典中
	responses[name] = response
	#看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_actve = False
#调查结束，显示结果
print ("\n--- Poll Resulte ---")
for name, response in responses.items():
	print (name + " would like to climb " + response + ".")
# 删除特定值的所有列表元素
# 在while循环中，删除多个同样的值。
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print (pets)
while 'cat' in pets:
	pets.remove('cat')
print (pets)

