'''with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)#输入完成之后，会在多了空白行因为.read()读到文件末尾时会返回一个空字符串。而将这个空字符串显示出来时就是一个空行。
	print(contents.rstrip())#文字末尾不换行，不显示空白行
	print(contents, end='')'''



'''逐行读取'''
'''
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())
'''

'''创建一个包含文件和行内容的列表'''
'''filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
		print (line.rstrip())
pi_string = ''
for line in lines:
	pi_string += line.strip()

print (pi_string)
print (len(pi_string))
'''