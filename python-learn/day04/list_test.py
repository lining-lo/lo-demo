"""
    列表
"""
# 创建列表
list1 = [1,2,3,4,5]
list2 = [1,'str',True,1,[2,3,4]]

# 获取数据
print("=======获取数据=======")
list3 = [0,1,2,3,4,5,6]
print(list3[0])
print(list3[3])
print(list3[-1])

# 切片操作
print("=======切片操作=======")
list4 = [0,1,2,3,4,5,6]
print(list4[0:3])
print(list4[0:-1])
print(list4[-3:6])
print(list4[2:])
print(list4[:4])
print(list4[:])
print(list4[::-1])
print(list4[::-2])
print(list4[5:0:-1])

# 基本操作
print("=======基本操作=======")
list5 = [1,2,4]
# 添加
list5.append(5)
print(list5)
# 插入
list5.insert(2,3)
print(list5)
# 合并
list6 = [7,8,9]
print(list5 + list6)
# 复制
print(list6 * 3)
# 是否存在
print(7 in list6)
# 列表长度
print(len(list6))
# 最大值
print(max(list6))
# 最小值
print(min(list6))
# 总和
print(sum(list6))

# 遍历列表
print("=======遍历列表=======")
list7 = [1,2,3,4]
# 方式 1
for i in list7:
    print(i)
# 方式 2
for i in range(len(list7)):
    print(list7[i])
# 方式 3
for k,v in enumerate(list7):
    print(k,v)

# 删除
print("=======删除=======")
list8 = [1,2,3,4,5,6,7,8,9]
# 单删
del list8[2]
print(list8)
# 多删
del list8[4:6]
print(list8)

# 嵌套列表
print("=======嵌套列表=======")
list9 = [[1,2,3],[4,5,6],[7,8,9]]
print(list9[1][1])
for i in list9:
    print(i)

# 列表推导示
print("=======列表推导示=======")
# 单列表
list10 = [i ** 2 for i in range(10)]
print(list10)
# 多列表
list11 = [1,2,3]
list12 = ["a","b","c"]
print([(x,y) for x in list11 for y in list12])

# zip函数
print("=======zip函数=======")
list13 = [1,2,3]
list14 = ["a","b","c"]
list15 = zip(list13, list14)
print(list(list15))