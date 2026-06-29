"""
  @Author:lining-lo
  @Time:2026/6/29
  @Desc:携程测试
"""
import asyncio


async def method1():
    print("携程方法开始执行")
    # 模拟异步任务耗时
    await asyncio.sleep(1)
    print("携程方法结束")


if __name__ == '__main__':
    res = method1()
    asyncio.run(res)
