"""
  @Author:lining-lo
  @Time:2026/6/24
  @Desc:输入输出流
"""


def method1():
    file1 = open("test.txt", "w", encoding='utf-8')
    file1.write("我滴老家~\n")
    file1.write("就住在这个屯~")
    file1.close()


# method1()

def method2():
    file2 = open("test.txt", "rt", encoding='utf-8')
    data = file2.read()
    print(data)
    file2.close()


# method2()


def method3():
    file3 = open("test.txt", "rt", encoding='utf-8')
    while True:
        data3 = file3.read(5)
        if data3 == "":
            break
        print(data3)
    file3.close()


# method3()

def method4():
    file4 = open("test.txt", "rt", encoding='utf-8')
    while True:
        data4 = file4.readline()
        if data4 == "":
            break
        print(data4)
    file4.close()


# method4()

def method5(org_src,tar_src):
    read_file = open(org_src,"rb")
    write_file = open(tar_src,"wb")
    while True:
        data = read_file.read(1024)
        if data == b"":
            break
        write_file.write(data)
    read_file.close()
    write_file.close()

# method5("D:\\test1.png","D:\\test2.png")


