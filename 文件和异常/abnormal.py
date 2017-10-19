'''
Python使用被称为“异常”的特殊对象来管理程序执行期间发生的错误。每当发生Python不知所措的错误时，
它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，
将显示一个traceback，其中包含有关的异常报告。
'''
#处理ZeroDivisionError异常
try:
	print(5/0)
# 将导致错误的代码放到Try中执行如果没问题将跳过下面的代码，如果有问题将执行下面代码
except ZeroDivisionError:
	print("You can't divide by zero!")



