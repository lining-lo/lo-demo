"""
  @Author:lining-lo
  @Time:2026/6/25
  @Desc:supper执行顺序
"""
class A:
    def method(self):
        print("A类中的method方法")

class B(A):
    def method(self):
        print("B类中的method方法")

class C(A):
    def method(self):
        super().method()
        print("C类中的method方法")

class D(C,B):
    pass

print(D.__mro__)
d = D()
d.method()