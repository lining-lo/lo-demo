"""
    循环
"""
from random import randint
from time import sleep

# while循环
progress  = 1
while progress <= 100:
    print(f"\r{'*' * progress}{progress}%",end="")
    step = randint(1,5)
    progress += step
    sleep(0.3)
else:
    print(f"\r{'*' * 100}100%")

# for循环
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}",end="\t")
    print()