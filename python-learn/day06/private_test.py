"""
  @Author:lining-lo
  @Time:2026/6/25
  @Desc:封装
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

p1 = Person('zhangsan',18)
print(p1.name)
print(p1.age)