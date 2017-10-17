'''with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)#输入完成之后，会在多了空白行因为.read()读到文件末尾时会返回一个空字符串。而将这个空字符串显示出来时就是一个空行。
	print(contents.rstrip())#文字末尾不换行，不显示空白行
	print(contents, end='')'''
'''逐行读取'''
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line)

