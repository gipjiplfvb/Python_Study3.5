magicians = ['alice', 'david', 'carolina']
#我们定义一个for循环；这行代码让python从列表magicians中取出一个名字，并其存储在变量magician中。最后我们让python打印前面存储的变量magician中的名字。这样对于列表中的每个名字，python都将重复执行magicians中每一个列表元素，
for magician in magicians:
	print (magician.title()  + ", that was great trick!")
	print ("I can't wait to see your next trick, " + magician.title() + ".\n")
	print ("Thank you, everyone. That was a great magic show!")
for i in magicians:
	print (i)
