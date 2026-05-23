"""
    输入输出
"""
# username = input("请输入账号：")
# password = int(input("请输入密码："))
# msg = "账号：%s,密码：%d" %(username,password)
# print(msg)

name = '张三'
age = 18
height = 1.8624
msg = "我是{}，今年{}，身高{:.2f}".format(name, age, height)
msg = f"我是{name=}，今年{age=}，身高{height=}"
print(msg)