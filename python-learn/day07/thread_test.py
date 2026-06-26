"""
  @Author:lining-lo
  @Time:2026/6/26
  @Desc:多线程
"""
import concurrent.futures
import threading
import time


def study():
    for i in range(1, 6):
        print(f"学习了{i}小时")
        time.sleep(0.5)


def play():
    for i in range(1, 6):
        print(f"玩了{i}小时")
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = threading.Thread(target=study)
    t2 = threading.Thread(target=play)
    t1.start()
    t2.start()


class Music(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(5):
            print(f"{self.name}正在听第{i}首歌")
            time.sleep(0.1)

if __name__ == '__main__':
    m = Music("咪咪")
    m.start()

def movie(name):
    print(f"{name}正在看电影")

if __name__ == '__main__':
    pool =  concurrent.futures.ThreadPoolExecutor(5)
    pool.submit(movie,"张三")
    pool.shutdown()