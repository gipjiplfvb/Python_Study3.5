#from PIL import Image
#import pytesseract
#img = Image.open(r'22.png')
#text = pytesseract.image_to_string(img)
#print (text)
#def lazy_sum(*args):
'''def su_m(args):
	ax = 0
	for n in args:
	#	print (n)
		ax = ax + n
	#	print (ax)
	return ax
	#return sum
	#print (su_m)
f = su_m([1, 3, 5, 7, 9])
print (f)'''

'''
def lazy_sum(*args):

	def su_m():
		ax = 0
		for n in args[0]:
			ax += n
		return ax

	return su_m()

f = lazy_sum([1, 3, 5, 7, 9])
print (f)

'''
'''
import getpass
_name = 'abc'
_passwd = 'abc123'
count = 0
while count<3:
    username = input("name:")
    passwd = input("passwd：")
    if _name == username	and _passwd == passwd:
        print("welcome user {name}  login...".format(name=username))
        break
    else:
        print("invalid username or password! Please Try Again")
    count += 1
else:
    print("您输入错误次数达到三次，请稍后再试！")
'''
a ="""
a *\ 20 
111111111111111
222222222222
33333333333
"""
print (a)