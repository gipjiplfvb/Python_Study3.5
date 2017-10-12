bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
#从列表bicycles中提取第一款自行车  注：在python中顺序是从0开始的。
print (bicycles[0])
#为了让结果看好看，整洁。
print (bicycles[0].title())
#python中为了访问最后一个列表元素提供了一种特殊的语法。通过奖索引指定为-1，可以让python返回最后一个列表元素。
print (bicycles[-1].title())
print (bicycles[-2])
print (bicycles[-3])
#从列表中提取第一款自行车，并使用这个值来创建一条消息：
message = "My first bicycle was a " + bicycles[0].title() + "."
print (message)
#习题将一些朋友的名字存储在一个列表当中，并为其命名为names依次访问该列表中的每个元素。
names = ["ma hao", "ma ting", "ma zeng", "ma shuang zeng", "ma liang"]
print (names[0].title())
print (names[1].title())
print (names[2].title())
print (names[3].title())
print (names[4].title())

message_1 = "\n" + (names[1].title()) + ":" + "\n\tHow are you ?"
print (message_1)
#修改列表元素
mototrcycles = ['hoda', 'yamaha', 'suzuki']
print (mototrcycles)
#修改列表中第一个元素
mototrcycles[0] = 'ducati'
print (mototrcycles)
#在列表末尾添加元素 .append
mototrcycles.append('hoda')
print (mototrcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print (motorcycles)
#插入一个元素到指定位置insert
motorcycles.insert(1, 'haojue')
print (motorcycles)
#删除列表中的一个元素de
del motorcycles[0]
print (motorcycles)
#方法pop()删除元素是从最后一个元素开始删除。
poped_motorcycles = motorcycles.pop()
print (poped_motorcycles)
print (motorcycles.pop())
print (motorcycles)
#.pop()使用方法，如果你的列表内容是按时间来排列的，可以使用这个参数打印出你最后输入的内容。()中可以输入数字，不能超过列表元素的总数。
motors = ['honda', 'bentian', 'haojue', 'qianjiang']
last_owned = motors.pop()
print ("The last motorcycle I owned was a " + last_owned.title() + ".")
#以上的参数都是可以根据索引删除列表中的元素，但是不能通过值来删除，现在我们来学习通过值来删除列表中的元素命令为remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)
motorcycles.remove('suzuki')
print (motorcycles)
#使用remove()从列表中删除元素时，也可接着使用它的值。下面删除值 “suzuki”，并打印一条删除，指出要将其从列表中删除的原因。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'jianshe']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print ("\nA " + too_expensive.title() + " is too expensive for me.")
guest_lst = ['laomao', 'laoma', 'laoliu', 'laohu']
guest_lst[0] = 'laoxi'
print ("我今天晚上要请这些人吃饭:\n" + str(guest_lst))
guest_lst = ['laomao', 'laoma', 'laoliu', 'laohu']
#因为laomao挂了，所以不能来吃饭了
poped_guest_lst = guest_lst.pop(0)
print ("because " + poped_guest_lst + " is die. So 不能来吃饭")
#使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print (cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print (cars)
#使用函数sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print ("Here is the original list:")
print (cars)
print ("\nHere is the sorted list:")
print (sorted(cars))
print ("\nHere is the sorted(reverse) list:")
print (sorted(cars, reverse = True))
print ("\nHere is the original list again:")
print (cars)
#reverse()永久性修改列表元素排列顺序，顺序是按列表中现有位置进行反转排列。
cars.reverse()
print (cars)
#确定列表长度可以使用参数len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (len(cars))
#练习
print (cars[2])