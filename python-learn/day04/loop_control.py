"""
    循环控制
"""
# continue
for i in range(0,21):
    if i % 2 != 0:
        continue
    else:
        print(f"{i}为偶数")

# break
sum = 0
for i in range(1,10):
    sum += i ** i
    print(sum)
    if sum >= 10000000:
        break

# pass 仅占位
flag = True
if flag:
    pass