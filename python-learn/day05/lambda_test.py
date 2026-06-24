"""
  @Author:lining-lo
  @Time:2026/6/24
  @Desc:lambda测试
"""
from functools import reduce


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def method1(a, b, method):
    return print(f"计算的结果是：{method(a, b)}")


method1(1, 2, sum)
method1(1, 2, sub)
method1(1, 2, lambda a, b: a + b)
method1(1, 2, lambda a, b: a - b)

stu_list = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 19},
]
result1 = sorted(stu_list, key=lambda x: x["age"])
print(result1)

list2 = [1, 2, 3, 4, 5]
result2 = list(map(lambda e: e * e, list2))
print(result2)

list3 = [1, -2, -3, -4, 5]
result3 = list(filter(lambda d: d > 0, list3))
print(result3)

list4 = [1,2,3,4,5]
result4 = reduce(lambda x, y: x + y, list4)
print(result4)
