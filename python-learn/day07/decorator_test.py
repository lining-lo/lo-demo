"""
  @Author:lining-lo
  @Time:2026/6/26
  @Desc:装饰器
"""
import math


def math_sqrt(n):
    return math.sqrt(n)


result = math_sqrt(4)
# result = math_sqrt(-4)
print(result)


def decorator(func):
    def inner(n):
        n = abs(n)
        return func(n)

    return inner


new_math_sqrt = decorator(math_sqrt)
result2 = new_math_sqrt(-4)
print(result2)

def decorator1(func,n):
    n = abs(n)
    return func(n)

result3 = decorator1(math_sqrt,-4)
print(result3)


def decorator2(func):
    def inner(n):
        n = abs(n)
        return func(n)

    return inner

@decorator2
def math_sqrt2(n):
    return math.sqrt(n)

print(math_sqrt2(-4))