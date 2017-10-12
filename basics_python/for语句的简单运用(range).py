
#在使用range()时，如果输出不符合预期，请尝试将指定值加1或减1
for value in range(1, 5):
	print (value)

numbers = list(range(1, 6))
print (numbers)
even_numbers = list(range(2, 11, 2))
print (even_numbers)
#range()几乎能创建任何需要的数字集，例如创建一个列表，其中包含前10个整数的平方。
squares = []
for value in range(11):
	square = value ** 2
	squares.append(square)
	print (squares)
#然而下面的代码更简洁。但使用临时变最能让代码更易读。
#你首先应该考虑的是，编写清晰易懂且能完成所需功能的代码；等到审核代码时，再考虑采用更高效的方法。
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print (squares)
#对数字列表执行简单的统计计算
digits = list(range(1, 1000000))
#print (digits)
digits.append(0)
#print (digits)
#print (min(digits))
#print (max(digits))
#print (sum(digits))
#squares = [value ** 2 for value in range(1, 11)]
#print (squares)


maxx = [val for val in range(1, 1000000)]
print (sum(maxx))

#下面是一个错误的例子，vals值对应range范围对单个整数。并不是一个列表，所以不能转为列表。
#for vals in range(1, 1000000):
#	vals_sum = list(vals)
#	print (sum(vals_sum))

lst = []
for vals in list(range(1, 1000000)):
	lst.append(vals)
print (sum(lst))


maxxx = sum(range(1, 10000000))
print (maxxx)
#print (help(sum))

a = [1, 2, 3, 4, 4]
print (type(a))