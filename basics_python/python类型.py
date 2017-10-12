age = 23
#message = "Happy " + age + "rd Birthday!"  #TypeError类型错误  age 是int（整数）类型，不能和str（字符串类型）进行运算
message = "Happy " + str(age) + "rd Birthday!"  #使用str()进行将非字符串类型转换成为字符串类型。
print (message)
print (4 + 4)
print (80 - 72)
print (2 * 4)
print (72 / 9)
age = 28
message = "My old is " + str(age)
print (message)

import this
