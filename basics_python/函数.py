# coding=utf-8

'''

def greet_user():
# 上面的代码行使用关键字def来告诉Python你要定义一个函数：这是函数的定义，向PYthon指出函数名，还可能在括号内指出函数为完成任务需要什么样的信息。在这里，函数名为greet_user()，它不需要任何信息就能完成其斯蒂芬和，因此括号是空的（即使如此，括号也是必不可少的)。最后，定义以冒号结尾。
	"""显示简单语句"""
	print ('Hello!')

greet_user()

#向函数传递信息
def greet_user(username):
	"""显示简单的问候语句"""
	print ("Hello, " + username.title() + "!")

greet_user('jesse')
# 实参和形参
# 形参：例子greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
# 实参：值'jesse'是一个实参。实参是调用函数时传递给函数的信息。
# 位置实参，这要求实参的顺序和形参的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。


#位置实参
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print ("\nI have a " + animal_type + ".")
	print ("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
	# 使用函数多次
describe_pet("dog", "willie")
	# 位置实参的顺序很重要
describe_pet('willie', 'dog')   #哈哈哈哈
#关键字实参
describe_pet(animal_type = 'hamster', pet_name = 'harry')
# 关键字实参的顺序不重要，因为Python知道各个值应该存储到那个形参中。
describe_pet(pet_name = 'harry', animal_type = 'hamster')
# 使用关键字实参时，务必准确地指定函数定义中的形参名。
# 默认值：编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，PYthon将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
def describe_pet(pet_name, animal_type = 'dog'):
	"""显示宠物的信息"""
	print ("\nI have a " + animal_type + ".")
	print ("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = 'willie')
# 让实参变成可选的
def get_formatted_name(first_name, middile_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + " " + middile_name + " " + last_name
	return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print (musician)
# 返回值
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。在函数中，可会用return语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()	# 将full_name的值转换为首字母大写格式，并将结果返回到函数调用行
# 调用返回值的函数时，需要提供一个变量，用于存储返回的值。在这里，将返回值存储在了变量musician中。输入为整洁的姓名：如下。
musician = get_formatted_name('jimi', 'hendrix')
print (musician)
# 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + " " +middle_name + " " +last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print (musician)

# 但并不是所有人的名字都是三个字的，我们可给实参middle_name指定一个默认值——空字符串，并在用户没有提供中间名时不使用这个实参。为让get_formatted_name()在没有提供中间名时依然可行，可给实参middle_name指定一个默认值——空字符串，并将其到形参列表的末尾。

def get_formatted_name(first_name, last_name, middle_name = ""):
	if middle_name:	#Python将非空的字符串解读为True，因此如果函数调用中提供中间名，ifmiddle_name将为True。
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' +last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print (musician)
musician = get_formatted_name('john', "hooker", 'lee')
print (musician)

# 返回字典
def build_person(first_name, last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print (musician)
# 当前字符串'jimi'和'hendrix'被标记为名和姓。你可轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或你要存储的其它任何信息。如下面的修改让你还能存储年龄。
def build_person(first_name, last_name, age = ''):
	"""返回一个字典，其中包含有关一个的信息。"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age = 27)
print (musician)


'''


# 结合使用函数和while循环
'''def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return  full_name.title()
# 这是一个无限循环
while True:
	print ("\nPlease tell me you name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print ("\nHello, " + formatted_name + "!")'''
# 这个while循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，该在什么地方退出呢？我们要让用户能尽可能容易的退出，因此每次提示用户输入时，都应该提供退出的途径。每次提示用户输入时，都使用break语句提供了退出循环的简单途径：
'''def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + " " + last_name
	return full_name.title()
while True:
	print ("\nPlease tell me your name: ")
	print ("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print ("\nHello, " + formatted_name + "!")'''
# 传递列表
# 假设有一个用户列表，我们要问候其中的每位用户。下面示例将一个名字列表传递给一个名为greet_users()的函数，这个函数问候列表中的每个人：
def greet_users(names):
	"""向列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print (msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# 在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效的处理大量的数据。

# 首先创建一个列表，其中包含一此要打印的设计
unprinted_designs = ['ipthone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 	打印每个设计后，将其移到列表completed_models中
while unprinted_designs:
	current_design = unprinted_designs.pop()

	# 模拟根据设计制作3D打印模型的过程
	print ("Printing model: " + current_design)
	completed_models.append(current_design)

# 显示打印好的所有模型
print ("\nThe following models have been printed:")
for completed_model in completed_models:
	print (completed_model)
# 为重新组织这些代码，我们可编写两个函数，每个都作一件具体的工作。大部分代码都与原来的相同，只是效率更高。第一个函数将负责处理打印设计的工作，而第二个将概述打印了那些设计：
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#模拟根据设计制作3D打印模型的过程。
		print ("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print ("\nThe following models have been printed:")
	for completed_model in completed_models:
		print (completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print (unprinted_designs[:])
# 传递任意数量的实参
def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print (toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 形参*toppings中的星号让Python创建一个名为toppings的空无级，并将收到的所有值都封闭在这个元组中。函数体内的print语句通过生成输出来证明Python能够处理使用一个值调用函数的情形，也能处理使用三个值调用函数的情形．它以类似的方式处理不同的调用，注意，Python将实参封闭在一个元组中，即使函数民到一个值也如此：
def make_pizza(*toppings):
	"""概述要制作的比萨"""
	print ("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print ("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 结合使用位置实参和任意数量实参
# 如果让函数接受不同类型的实参，必需在函数定义中将接纳任务数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# e.g 如果前面的函数还需要一个表示比萨尺寸的实参，必需将形参放在形参*toppings的前面：
def make_pizza(size, *toppings):
	"""概述要制作的比萨"""
	print ("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstenin',
							 location = 'princeton',
							 field = 'physics')

print (user_profile)
#  形参**user_info中的两个星号是让Python创建一个名为user_info的空字典，并将收到所有名称-值对都封装到这个字典中。在这个函数中，可以像访问其它字典那样访问user_info中的名称-值对。
from 基础.pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 也就是xxx是一个文件这个文件里面存在一个或着多个函数，yy是文件中函数的名称。
# from XX import y_1, y_2, y3
# 可以引用一个  也可以同时引用多个

# 使用as给函数指定别名

# 如果导入的函数的名称可能与程序中现有的名称冲突，或者函数的名字太长，可指定简短而独一无二的别名————函数的另一个名称，类似于外号。要给函数指定这种特殊的外号，需要在导入它时这样做。
from 基础.pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
#
