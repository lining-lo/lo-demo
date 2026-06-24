"""
  @Author:lining-lo
  @Time:2026/6/24
  @Desc:深浅拷贝
"""
import copy

list1 = [1, 2, 3, ]
print("list1", list1)
list2 = list1
list2[1] = 200
print("list2", list2)
print("list1", list1)

list3 = [4, 5, 6]
print("list3", list3)
list4 = list3.copy()
list4[1] = 500
print("list4", list4)
print("list3", list3)

list5 = [7, 8, [9, 10, 11]]
print("list5", list5)
list6 = list5.copy()
list6[2][0] = 900
print("list6", list6)
print("list5", list5)


list7 = [12, 13, [14, 15, 16]]
print("list7", list7)
list8 = copy.deepcopy(list7)
list8[2][0] = 1400
print("list8", list8)
print("list7", list7)