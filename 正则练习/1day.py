#import re
#print(re.match('www', 'www.runoob.com').span())
#print(re.match('com', 'www.runoob.com'))
'''
i = 1
result = 1
while i<= 100:
	result = result * i
	i += 1

print (result)'''
'''
def test(num):
	if num > 1:
		return 	num * test(num - 1)
	else:
		return 1
a = test(100)
print (a)
'''
print("Hello, World")