"""
  @Author:lining-lo
  @Time:2026/6/25
  @Desc:继承
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}正在叫")


class Dog(Animal):
    def house_sit(self):
        print(f"{self.name}正在看家")

    def speak(self):
        print(f"{self.name}正在汪汪叫")


a1 = Animal("timi")
print(a1.name)
a1.speak()

d1 = Dog("旺财")
print(d1.name)
d1.speak()
d1.house_sit()


class Cat(Animal):
    def speak(self):
        print(f"{self.name}正在喵喵叫")


class Pet(Cat, Dog):
    def speak(self):
        print(f"{self.name}正在嘤嘤叫")


p1 = Pet('小米')
p1.speak()


