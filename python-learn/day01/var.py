"""
    变量学习
"""

var = '变量'
var = 1
print(var)

# var1 = 100
# var2 = 100
# var3 = 100
var1 = var2 = var3 = 100
print(var1, var2, var3)

# var1 = 100
# var2 = 200
# var3 = 300
var1,var2,var3 = 100,200,300
print(var1,var2,var3)

"""
    变量命名：
        ①只能用字母、数字（不能开头）、下划线
        ②不能用关键字
        ③区分大小写
"""
__aabb = 1
import keyword
print(keyword.kwlist)

# 大驼峰
UserName = "大驼峰"
# 小驼峰
userName = "小驼峰"
# 蛇形命名
user_name = '蛇形命名'
# 常量
USERNAME = '常量'