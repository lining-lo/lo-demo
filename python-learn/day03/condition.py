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