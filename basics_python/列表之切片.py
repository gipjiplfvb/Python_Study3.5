players = ['charles', 'martina', 'michael', 'florence', 'eli']
#取列表players中第1，2，3的值，起始位置是0结束位置是3
print (players[0: 3])
#如果没有第一个索引，则默认从列表开头开始：
print (players[: 3])
#要让列表终止于末尾，也可以用上面类似的语法来表示
print (players[2:])
#无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素。够数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片。如果你想要后三个元素的话：
print (players[-3:])
#遍历切片
print ("Here are the first three players on my team:")
for player in players[: 3]:
	print (player.title())
#复制列表
#要复制列表，可创建一个包含数个列表的切片，方法是省略起始索引和终止索引([:])。让python创建一个始于第一元素，终止于最后一个元素的切片，即复制整个列表。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print ("My favorite foods are:")
print (my_foods)

print ("\nMy friend's favorite foods are:")
print (friend_foods)
