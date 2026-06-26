"""
  @Author:lining-lo
  @Time:2026/6/26
  @Desc:类装饰器
"""
import math


class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        x = abs(x)
        return self.func(x)


def math_sqrt(num):
    return math.sqrt(num)


d1 = DecoratorClass(math_sqrt)
print(d1(-4))

@DecoratorClass
def math_sqrt2(num):
    return math.sqrt(num)

print(math_sqrt2(-9))