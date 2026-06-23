"""
  @Author:lining-lo
  @Time:2026/6/23
  @Desc:集合测试
"""
set1 = {"张三","李四","王五"}
print(set1)

set2 = set(['高','大','壮'])
print(set2)

set3 = {i for i in range(1,11)}
print(set3)

set4 = {}
print(type(set4))

set5 = set()
print(type(set5))

set6 = {"小龙女"}
set6.add("伊志平")
set6.add("杨过")
print(set6)
set6.remove("伊志平")
print(set6)
print("伊志平" in set6)
print(len(set6))

set7 = {1,2,3,4,5}
print(max(set7))
print(min(set7))
print(sum(set7))

set8 = {"天","下","无","敌"}
for i in set8:
    print(i,end="\t")
print()
for index,element in enumerate(set8):
    print(index,element,end="\t")
print()

set9 = {"一","二","三"}
set9.add("四")
print(set9)
set9.update(["五","六"])
print(set9)
set10 = set9.union(["七","八"])
print(set10)
set10.remove("一")
print(set10)
set10.discard("三")
print(set10)
set10.clear()
print(set10)

set11 = {"张三","李四","王五","赵六"}
set12 = {"张三","李四"}
print(set11.difference(set12))
set11.difference_update(set12)
print(set11)

set13 = {"张","李","王","赵"}
set14 = {"张","王"}
print(set13.intersection(set14))
set13.intersection_update(set14)
print(set13)

set15 = {"a","b","c","d"}
set16 = {"a","b"}
print(set15 & set16)
print(set15 | set16)
print(set15 - set16)
print(set15.isdisjoint(set16))
print(set15.symmetric_difference(set16))
set15.symmetric_difference_update(set16)
print(set15)

set17 = {"更高","更快","更强"}
set18 = set17.copy()
print(set18)