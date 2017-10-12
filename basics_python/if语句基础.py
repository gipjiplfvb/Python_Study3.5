#下面代码遍历一个列表，并以道字母大写的方式打印其中的汽车名，但对汽车名"bmw" ，以全大写的方式打印
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print (car.upper())
	else:
		print (car.title())
#检查是否相等
car = 'bmw' # = 先赋值
print (car == 'bmw')    # == 再判断
car = 'audi'
print (car == 'bmw')
#检查是否相等时不考虑大小写
car = 'Audi'
print (car == 'audi')   #两个值大小写不同时会被视为false
#如果大小写很重要，这种行为有其优点，但如果大小写无关紧要，而只是想检查变量的值，可将变量值转换为小写，再进行比较。
car = 'Audi'
print (car.lower() == 'audi')   #函数lower()不会改变变量car中的值。
print (car)
#检查是否不相等，“!=”表示“不”
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print ("Hold the anchovies!")
#比较数字
age = 18
print (age == 18)
answer = 17
#在条件语句中可包含和种数学比较，如小于、小于等于、大于、大于等于：
if answer !=42:
	print ("That is not the correct answer. Please try again!")
#检查多个条件
#and语句 要检查是否两个条件都为Ture，可使用关键字and将两个条件测试合而为一；如果每个测试都通过了，整个表达式为Ture；如果至少有一个测试没有通过，则整个表达式就是False。
age_0 = 22
age_1 = 18
print (age_0 >= 21 and age_1 >= 21)
age_1 = 22
print (age_0 >= 21 and age_1 >= 21)
#or 也能够让你检查多个条件，但要至少有一个条件满足，就能通过测试。仅当两个测试都没通过时，使用or的表达方式才为False。
age_0 = 22
age_1 = 18
print (age_0 >=21 or age_1 >= 21)
age_0 = 18
print (age_0 >=21 or age_1 >=21)
#检查特定值是否包含在列表中 in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print (user.title() + ", you can post a response if you wish")

car = 'audi'
print ("Is car == 'subaru'? I predict True.")
print (car == 'subaru')
if car == 'subaru':
	print ("False")
else:
	print ("Ture")
age = 19
if age >= 18:
	print ("You are old enough to vote!")

age = 19
if age >= 18:
	print ("You are old enough to vote!")
	print ("Have you registered to vote yet?")

# if - else语句
age = 17
if age >= 18:
	print ("You are old enough to vate!")
	print ("Have you registered to vote yet")
else:
	print ("Sorry, you are too young to vote.")
	print ("Please register to vote as soon as you turn 18!")
#if elif else 结构
#经常需要检查超过两个情形，为此可使用Python提供的if- elif - else Python只执行if- elif- else结构中一个代码块，它依次检查每个条件测试，真到遇到通过了条件测试。测试通过后，Python将捃紧跟在后面的代码，并跳过余下的测试。
age = 12
if age < 4:
	print ("Your admission cost is $0.")
elif age < 18:
	print ("Your admission cost is $5.")
else:
	print ("Your admission cost is $10.")
#如上段代码，简洁写法
#以上代码使用if-elif-else结构作用更小，但效率更高，代码容易修改：要调整输出的消息内容，只需要修改一条，而不是三条print语句。
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print (type(price))
print ("Your admission cost is $" + str(price) + ".")
#使用多个elif代码块。
age = 112
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 1
print ("Your admissoon cost is $" + str(price) + ".")
#Python并不要求if-elif结构后面必需有else代码块。在有些情况下，else代码块很有用；而在其它一些情况下，使用elif语句来处理特定的情形更清晰。
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
print ("Your admission cost is $" + str(price) + ".")
#如上。else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应该考虑使用一个elif代码块来代替else代码块。这样你就可以肯定，仅当满足相应在的条件时，你的代码才会执行。

print ("\n测试多个条件\n")
#if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了测试后，Python就跳过余下的测试。这种行为很好，效率很高，让你就能够测试一个特定的条件。
#然而，有时候必需检查你关心的所有条件。在这种情况下，应该使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。
reguested_toppings = ['mushrooms', "extra cheese"]
if 'mushrooms' in reguested_toppings:
	print ("Adding mushrooms.")
if 'pepperoni' in reguested_toppings:
	print ("Adding popperoni.")
if 'extra cheese' in reguested_toppings:
	print ("Adding extra cheese")
print ("\nFinished making your pizza!")
print ("***********************************")
#如果某一个元素没有，或着用完了
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for reguested_topping in requested_toppings:
	if reguested_topping == 'green peppers':
		print ("Sorry, we are out of greed poppers right now.")
	else:
		print ("Adding " + requested_topping + ".")
print ("\nFinished making your pizza!")
#确定列表不是空的
print ("***********************************")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_tppings:
		pring ("Adding " + requested_topping + ".")
	print ("\nFinished making you pizza")
else:
	print ("Are you sure you want a plain pizza?")

print("***********************************")
#使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print ("Adding " + requested_topping + ".")
	else:
		print ("Sorry, we don't have " + requested_topping + ".")
print ("\nFinished making your pizza!")
