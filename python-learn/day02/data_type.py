"""
    1.数据类型
        数值类型：整型(int)、浮点(float)、复数(complex)、布尔(bool)
        容器类型：列表(list)、元组(tuple)、集合(set)、字典(dict)
        None
    2.是否可变
        可变数据类型：列表、字典、集合
        不可变数据类型：数值、字符串、元组
    3.type、isinstance 和 is 可以判断数据类型
    4.浮点类型会有精度丢失问题，可以用 Decimal(数值字符串) 函数解决
    5.布尔继承了 int ,true(1),false(0)
"""
from decimal import Decimal

# instance
print(isinstance(1, int))
print(isinstance(True,int))
print(isinstance(1.1,int))
print("======================")

# type
a = 1
b = 2.2
c = True
d = (4,5,6)
e = [7,8,9]
f = {10,11,12}
g = {'k1':'v1','k2':'v2'}
h = 'str'
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(a) == type(b))
print(type(a) == type(c))
print("======================")

# is
i = 'a'
j = 2
k = False
l = 2
print(i is j)
i = j
print(i is j)
print(j is l)
print(id(i))
print(id(l))
print("======================")

# 整型可以可以表示任意大小，可以用_连接增加可读性
print(123456789123456789)
print(1_000_000 == 1000000)
print("======================")

# float
f1 = 0.1
f2 = 0.2
print(f1 + f2)
print(Decimal("0.1") + Decimal("0.2"))
print("======================")

# bool
print(True == 1)
print(False == 0)
print(1 + False)
print(1 + True)
print(True is 1)
print(type(True) == type(1))
print("======================")

# 字符串
str1 = "我爱’我国"
str2 = '我爱"我家'
print(str1)
print(str2)
str3 = ("select "
        "* "
        "from student "
        "where id = '111'")
str4 = "select \
        * \
          from student \
        where id = '111'"
str5 = """
        select 
            * 
            from student 
            where id = '111'
"""