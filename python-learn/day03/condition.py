"""
    条件语句
"""
from random import randint

# 单分支
balance = randint(1, 100)
price = 50
print(f"当前余额：{balance}")
if balance < price:
    print("余额不足")
else:
    print(f"购买成功，剩余余额：{balance - price}")
print("欢迎下次光临")
print("\n")

# 多分支
score = randint(0, 100)
print(f"{score=}")
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("请继续续努力")
print("\n")

# 嵌套分支
# username = input("请输入用户名：")
# if username == "admain":
#     password = input("请输入密码：")
#     if password == "123456":
#         print("登录成功")
#     else:
#         print("密码错误")
# else:
#     print("账号不存在")
# print("\n")

# match
day = randint(0,10)
print(f"{day=}")
match day:
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case 4:
        print('星期四')
    case 5:
        print('星期五')
    case 6:
        print('星期六')
    case 7:
        print('星期天')
    case _:
        print('数据错误')
print("\n")

# 三元运算符
flag = True
print("选项一" if flag else "选项二")
print("\n")