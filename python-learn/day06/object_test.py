"""
  @Author:lining-lo
  @Time:2026/6/24
  @Desc:面向对象
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}在吃饭")

    def get_self(self):
        print(f"self：{id(self)}")

p1 = Person("张三", 20)
print(p1.name, p1.age)
p1.eat()
print(id(p1))
p1.get_self()