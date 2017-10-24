"""
为了核实name_function.py文件中get_formatted_name()像期望的那样工作，
我们来编写一个使用这个函数的程序。本程序让用户输入名和姓，并显示整洁的全名。
"""
from name_function import get_formatted_name
print ("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("\nPlease give me a last name: ")
	if last == 'q':
		break
	formatted_name = get_formatted_name(first, last)
	print ("\nNeatly formatted name: " + formatted_name + '.')

