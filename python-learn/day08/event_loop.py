"""
  @Author:lining-lo
  @Time:2026/6/29
  @Desc:事件循环
"""
import asyncio


async def method1():
    print("<start>协程任务1开始执行")
    await asyncio.sleep(2)
    print("<end>协程任务1执行结束")


async def method2():
    print("<start>协程任务2开始执行")
    await asyncio.sleep(2)
    print("<end>协程任务2执行结束")


async def main():
    task1 = asyncio.create_task(method1())
    task2 = asyncio.create_task(method2())

    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())
