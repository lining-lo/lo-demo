"""
  @Author:lining-lo
  @Time:2026/6/23
  @Desc:冒泡排序和二分查找
"""


def method1(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


result = method1([5, 4, 3, 2, 1])
print(result)


def method2(list, n):
    if n < 1:
        return list
    for i in range(0, n):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    return method2(list, n - 1)


list = [5, 4, 3, 2, 1]
result2 = method2(list, len(list) - 1)
print(result2)


def method3(list, target):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = (max + min) // 2
        if list[mid] > target:
            max = mid - 1
        elif list[mid] < target:
            min = mid + 1
        else:
            return mid
    return -1


result3 = method3([11, 22, 33, 44, 55, 66, 77, 88, 99], 55)
print(result3)
