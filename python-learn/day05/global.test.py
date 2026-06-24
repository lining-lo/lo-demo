"""
  @Author:lining-lo
  @Time:2026/6/23
  @Desc:global关键字及递归
"""
num = 10


def method1():
    global num
    num = num + 10
    print(num)


method1()


def method2(n):
    if n == 1:
        print(1)
        return
    print(n)
    n -= 1
    method2(n)


method2(3)


def method3(n):
    if n == 1:
        return 1
    return n * method3(n - 1)


result = method3(5)
print(result)


def method4(n):
    if n == 1 or n == 2:
        return 1
    return method4(n - 1) + method4(n - 2)


result2 = method4(12)
print(result2)
