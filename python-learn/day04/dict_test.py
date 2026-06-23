"""
  @Author:lining-lo
  @Time:2026/6/23
  @Desc:字典测试
"""
dict1 = {}
print(dict1)

dict2 = dict()
print(dict2)

dict3 = {"name": "张三", "age": 18, "height": 182}
print(dict3)

dict4 = dict(name="iphone", type=13)
print(dict4)

dict5 = {"苹果": 5.99, "香蕉": 3.50, "面包": 8.80}
print(dict5["面包"])
print(dict5.get("苹果"))
dict5["牛奶"] = 4.20
print(dict5)
dict5["牛奶"] = 4.50
print(dict5)
del dict5["香蕉"]
print(dict5)
dict5.clear()
print(dict5)
del dict5
# print(dict5)

dict6 = {"name": "曹操", "age": 24, "weight": 100, "hobby": "人妻"}
print("name" in dict6)
print(len(dict6))
keys = dict6.keys()
print(keys, type(keys))
for key in keys:
    print(key, dict6[key])
values = dict6.values()
print(values, type(values))
for value in values:
    print(value)
items = dict6.items()
print(items, type(items))
for item in items:
    print(item[0], item[1])

dict7 = {"name": "良子", "age": 30, "weight": 400, "hobby": "板面和焖子"}
print(dict7.pop("age"))
print(dict7)
print(dict7.popitem())
print(dict7)
dict8 = {"hight":'165',"father":"buzhidao"}
dict7.update(dict8)
print(dict7)
dict7.setdefault("name")
dict9 = dict7.copy()
print(dict9)
