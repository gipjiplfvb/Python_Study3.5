'''异常处理'''
'''ZerDivisionError 错误
print("Give me two numbers, and I'll divide them.")
print ("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number.")
	if first_number == "q":
		break
	second_number = input("Second number:")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) /int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero")
	else:
		print(first_number + "/" + second_number + "=" + str(answer))
		#print(answer)
'''
#---------------------------------------------------------------------------
'''FileNotFoundError
filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist"
	print(msg)
	'''
#---------------------------------------------------------------------------
'''分析文本
filename = "55767-0.txt"
try:
	with open(filename, encoding='utf-8') as f_objt:
		contents = f_objt.read()
except FileNotFoundError:
	msg = "Sorry, the file" + filename + "does not exist."
	print(msg)
else:
	#计算文件大概有多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words!")
	'''
#-----------------------------------------------------------------------------
'''计算一个文件有多少个单词'''
'''def coun_words(filename):
	try:
		with open(filename, encoding='utf-8') as file_o:
			contents = file_o.read()
	except FileNotFoundError:
		msg = "找不到%s这个文件"%(filename)
		print(msg)
	else:
		word_s = contents.split()
		num_word_s = len(word_s)
		print("这个文件%s一共有%d个单词"%(filename, num_word_s))
a = '55767-0.txt'
coun_words(a)
#------------------------------------------------------------------------------
#使用多个文件
filenames = ['55767-0.txt', 'divsion.py', 'pi_million_digits.txt', 'fuck.txt']
for b in filenames:
	coun_words(b)
'''
#-------------------------------------------------------------------------------
'''失败时一声不吭'''
def coun_words(filename):
	try:
		with open(filename, encoding='utf-8') as file_o:
			contents = file_o.read()
	except FileNotFoundError:
		#pass
		# pass语句充当占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做什么。
		with open('miss_msg.txt', 'w', encoding='utf-8') as msage:
		#当找不到某个文件时，输出的信息不让用户看到这个提示信息，但是后台要记录下来。
				msage.write('这个文件%s找不到'%(filename))

	else:
		word_s = contents.split()
		num_word_s = len(word_s)
		print("这个文件%s一共有%d个单词"%(filename, num_word_s))
print("-"*30)
filenames = ['55767-0.txt', 'divsion.py', 'pi_million_digits.txt', 'fuck.txt']
for b in filenames:
	coun_words(b)


print ('a' == 'a')
