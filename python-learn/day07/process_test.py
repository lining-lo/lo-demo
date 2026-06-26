"""
  @Author:lining-lo
  @Time:2026/6/26
  @Desc:多进程
"""
import time
from multiprocessing import Process
import multiprocessing


def coding(name, count):
    for i in range(count):
        print(f"{name}写代码中...{i + 1}")


def music(name, count):
    for i in range(count):
        print(f"{name}听音乐中...{i + 1}")


if __name__ == '__main__':
    p1 = Process(target=coding, name="进程1", args=("张三", 6))
    p2 = Process(target=music, name="进程2", kwargs={"name": "李四", "count": 3})

    # p1.start()
    # p2.start()


class swimming(Process):
    def run(self):
        for i in range(10):
            print(f"游泳中...{i + 1}")


if __name__ == '__main__':
    # swimming().start()
    pool = multiprocessing.Pool(5)
    # pool.apply(coding,args=(("张三",5)))
    pool.apply_async(coding,args=(("张三",5)))

    pool.close()
    pool.join()
