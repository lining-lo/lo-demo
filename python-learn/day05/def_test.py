"""
  @Author:lining-lo
  @Time:2026/6/23
  @Desc:方法测试
"""


def sum():
    a = 10
    b = 20
    sum = a + b
    print(sum)


sum()


def sub(a: int, b: int):
    print(a - b)


sub(a=10, b=20)


def mul():
    a = 10
    b = 20
    return a * b


result = mul()
print(result)


def div(a, b):
    return a / b


print(div(a=10, b=20))


def method1(a, b):
    return a + b


def method2():
    a = 10
    b = 20
    result = method1(a, b)
    print(result)


method2()


def speak(name, /, *, sex, age):
    print(f"我叫{name},是个{sex}生，今年{age}岁")


speak("张三", sex="女", age=18)


def method3(*args):
    print(args)


method3(1, 2, 3)


def method4(**kwargs):
    print(kwargs)


method4(name="zhang", age=18)


def method5(name, **kwargs):
    print(name, kwargs)


method5("lisi", age=18, hobby="rap")


def method6(a, b, c):
    print(a, b, c)


method6(*(1, 2, 3))
method6(*[4, 5, 6])
method6(**{"a": "张三", "b": "李四", "c": "王五"})
