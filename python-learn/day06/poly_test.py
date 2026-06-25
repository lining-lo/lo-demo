"""
  @Author:lining-lo
  @Time:2026/6/25
  @Desc:多态
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('动物吃饭')


class Dog(Animal):
    def eat(self):
        print("小狗吃骨头")

    def look_house(self):
        print("小狗看家")

class Cat(Animal):
    def eat(self):
        print("小猫吃鱼")
    def catch_mouse(self):
        print("小猫抓老鼠")


def method(animal):
    animal.eat()
    if isinstance(animal,Dog):
        animal.look_house()
    elif isinstance(animal,Cat):
        animal.catch_mouse()
    else:
        print("无效参数")

d1 = Dog("旺财")
method(d1)
c1 = Cat("咪咪")
method(c1)
