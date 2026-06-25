"""
  @Author:lining-lo
  @Time:2026/6/25
  @Desc:异常处理
"""


def add():
    9 / 0
    print("添加功能")


try:
    add()
except Exception as e:
    print("\033[91m出现异常：", e, "\033[0m")
finally:
    print("这里一定会执行")

print("删除功能")
print("修改功能")
print("查找功能")


def int_sum(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("参数类型错误")


int_sum(1, 2)


class MyException(Exception):
    def __init__(self, message):
        self.message = message


def method1():
    try:
        1 / 0
    except Exception as e:
        raise MyException("自定义异常")


method1()
