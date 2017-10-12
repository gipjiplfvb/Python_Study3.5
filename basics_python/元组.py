#列表非常适合用于存储在程序运行期间可能变化的数据集，列表是要以修改的，这对处理网站的用户列表和游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，元组可以满足你这种需求。python将不能修改的值称为不可变的，而不可变的列表被称为“元组”
#元组看起来犹如列表，但使用园括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表一样。
dimensions = (200, 50)
print (dimensions[0])
print (dimensions[1])
#下面代码是有错误的，由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值：
#dimensions[0] = 250
#print (dimensions)


#遍历元组中的所有值，像列表一样，也可以使用for循环来遍历元组中的所有值：
dimensions = (200, 500, 210)
for dimension in dimensions:
	print (dimension)
#修改元组变量，虽然元组中的元素不能修改，但是可以给存储无组的变量赋值。因此，如果修改前述矩形的尺寸，可重新定义整个元组：
dimensions = (290, 47)
print ("Original dimensions:")
for dimension in dimensions:
	print (dimension)

dimensions = (300,200)
print ("\nModified dimensions:")
for dimension in dimensions:
	print (dimension)



