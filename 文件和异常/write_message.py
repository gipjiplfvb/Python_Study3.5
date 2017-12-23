'''写入文件'''
filename = "programming.txt"
with open(filename, 'w') as file_object:
	file_object.write("I Love Python.\n")
	#要写入多行内容，就继续上面的代码
	file_object.write("I love creating new games.\n")
	'''重要的事说三遍'''
#注：python中只能将字符串写入文本文件。要将数值数据存储到文本文件中，必需为字符串格式
#注：python中只能将字符串写入文本文件。要将数值数据存储到文本文件中，必需为字符串格式
#注：python中只能将字符串写入文本文件。要将数值数据存储到文本文件中，必需为字符串格式
	file_object.write("135464687645264687645.\n")
#'r'为只读,'w'为写,'a'为续写。
a = input("测试一下文件录入：")
with open(filename, 'a', encoding='utf-8') as file_object:
	file_object.write("I like Pycharm IDE.\n")
	file_object.write(a,)
