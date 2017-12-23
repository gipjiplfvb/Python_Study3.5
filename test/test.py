'''def fib(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print (fib(50))'''
'''
def hlt(n, x, y, z):
	if n == 1:
		print(x, '--->', z)
	else:
		hlt(n - 1, x, z, y)
		hlt(1, x, y, z)
		hlt(n - 1 , y, x, z)
print(hlt(3, '左', '中', '右'))
'''
#coding=gbk
import chardet

def main():
    """ """

    name = input("please enter:" )
    result = chardet.detect(name.encode("utf-8"))
    print(result)

if __name__ == "__main__":
    main()
