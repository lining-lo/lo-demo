"""
  @Author:lining-lo
  @Time:2026/6/24
  @Desc:面向对象
"""
import types


class Person:
    """
    这是一个人类
    """
    classroom = 'T506'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}在吃饭")

    def get_self(self):
        print(f"self：{id(self)}")

    @classmethod
    def method(cls):
        print(cls.__dict__)
        print(cls.__doc__)


p1 = Person("张三", 20)
print(p1.name, p1.age)
p1.eat()
print(id(p1))
p1.get_self()

print(Person.classroom)
Person.classroom = 'T505'
print(Person.classroom)

Person.method()

p1.weight = 140
print("动态添加实例属性", p1.weight)

Person.grade = "高一"
print("动态添加类属性", Person.grade)


def drink():
    print("动态添加普通方法 喝水")


p1.drink = drink
p1.drink()


def wc(self):
    print("动态添加实例方法", f"{self.name}上厕所")


p1.wc = types.MethodType(wc, p1)
p1.wc()


@staticmethod
def static_method():
    print("动态添加静态方法")


Person.static_method = static_method
Person.static_method()


@classmethod
def class_method(cls):
    print("动态添加类方法", cls.__doc__)


Person.class_method = class_method
Person.class_method()


class ArrayUtils:
    @staticmethod
    def getSum(*arr):
        sum = 0
        for i in arr:
            sum += i
        return sum


print(ArrayUtils.getSum(1, 2, 3, 4))
