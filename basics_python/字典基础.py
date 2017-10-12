'''lst = [["a", 1],["b", 2], ["c", 3], ["d", 1]]
print (lst)
print (dict(lst))
test = dict(lst)
print (test)

test_1 = [val for kay,val in lst]
print (test_1)
print (type(test_1))
#if test_1[range(len(test_1))] == test_1[range(1,len(test))]
#	print (ture)



resList = [];
resList1 = [1,2,3,1,3]
resList2 = []
for i in range(len(resList1)):
    if(resList1.count(resList1[i]) >=2 ):
        if(resList2.count(resList1[i]) >= 1):
            continue
        else:
            resList2.append(resList1[i])
print (resList2)'''

alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])
new_points = alien_0['points']
print ("You just earned " + str(new_points) + " points!")
print (alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print (alien_0)
print ("********************************")
alien_0 = {'x_position': 0, "y_position": 25, 'speed': 'medium'}
print ("Original x-position: " + str(alien_0['x_position']))
# 向左移动外星人
# 据外星人当前的速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这外外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print ("New x-position: " + str(alien_0['x_position']))
# 删除键值对  删除的键-值对将永远消失
print ("删除键值对*********************")
alien_0 = {'color': 'green', 'points': 5}
del alien_0['color']
print (alien_0)
#由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', #最后面的逗号，为以后在下一行添加键-值对做好准备。
    }
# 对于大多数编辑器都以类似的方式设置其格式的功能。对于较长的字典，还有其它一些可行的格式设置试，因此在你的编辑器或其它源代码中，你可能会看到稍微不同的格式设置方式。
print (favorite_languages)
print ("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
a = favorite_languages['sarah']
#   遍历所有的键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print ("\nKey: " + key)
    print ("Value: " + value)

for name, language in favorite_languages.items():
    print (name.title() + "'s favorite language is " + language.title() + ".")
print ("**********************")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print (name.title())
    if name in friends:
        print (" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
print ("//////////////////////////////")
if 'erin' not in favorite_languages.keys():
    print ("Erin ,please take our poll!")
print("******************************")
# 遍历字典中的所有键。
for name in sorted(favorite_languages.keys()):
    print (name.title() + ", thank you for taking the poll.")
# 遍历字典中的所有值。
print ("****************")
print ("The fllowing langueages have been mentioned:")
for language in favorite_languages.values():
    print (language.title())
# 通过对包含重复元素的列表调用set()，可让Python找到列表中独一无二的元素，并使用这些元素来创建一个集合。
for language in set(favorite_languages.values()):
    print (language.title())
# 字典的嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print (aliens)
for alien in aliens:
    print (alien)
# 更符合现实的情形是，外星人不止三个，且每个外星人都使用代码自动生成的。在下面的救命中，我们使用range()生成了30个外星人：
# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print (alien)
print ("...")
# 显示创建了多少个外星人。
print ("Total number of aliens: " + str(len(aliens)))
for alien in aliens[0: 3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
for alien in aliens[0: 5]:
    print (alien)
print ('...')
# 在字典中存储字典
users = {
    'aeinstein':{
        'first': 'ma',
        'last': 'li',
        'location': 'zhang',
        },
    'mcurie':{
        'first': 'hang',
        'last': 'hei',
        'location': 'si',
        },
    }
for username, user_info in users.items():
    print ("\nUsername: " + username)
    full_name  = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print ("\tFull name: " + full_name.title())
    print ("\ttlocation: " + location.title())

