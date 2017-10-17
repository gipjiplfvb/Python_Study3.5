#from collections import OrderedDict

#favorite_languages = OrderedDict()
#favorite_languages
numbers={'a':'111','b':'222','c':'333','d':'444',}
list_1 = []
for key, value in numbers.items():
	print (type(key))
	list_1.append(str(key))
	print (type(key))
print (list_1)
for i in range(2):
	print
	del numbers[list_1[i]]
print (numbers)


#key = 1
#while key <= 2:
#	del numbers[(str(key))]
#	key += 1
#print (numbers)
