"""
  @Author:lining-lo
  @Time:2026/6/22
  @Desc:元组练习
"""

tuple1 = ("张三", "李四", "王五")
print(tuple1, type(tuple1))

# tuple2 = (1)
tuple2 = (1,)
print(tuple2, type(tuple2))

tuple3 = (i for i in range(0, 10))
tuple4 = tuple(tuple3)
print(tuple3, type(tuple3))
print(tuple4, type(tuple4))

tuple5 = ("张三", "李四", "王五", "赵六")
print(tuple5[2])
print(tuple5[1:3])

tuple6 = ('我', "爱")
tuple7 = ('中', '华')
print(tuple6 + tuple7)
print(tuple7 * 3)
print(len(tuple7))

tuple8 = (1, 2, 3, 4, 5)
print(max(tuple8))
print(min(tuple8))
print(sum(tuple8))

tuple9 = ("我", "滴", "老", "家")
for i in tuple9:
    print(i)
for j in range(len(tuple9)):
    print(tuple9[j])
for index, element in enumerate(tuple9):
    print(index, element)

tuple10 = (1, 2, 3, 4, 5)
# tuple10[1] = 20
tuple11 = tuple(tuple10) + (6, 7)
print(id(tuple10), id(tuple11))

tuple12 = (1, 2, [3, 4])
tuple12[2][0] = 200
print(tuple12)
