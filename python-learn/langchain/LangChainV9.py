"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:异步普通调用_invoke
"""
# 1.导入依赖
import os
from langchain.chat_models import init_chat_model
import asyncio

# 2.实例化模型
model = init_chat_model(
    model="qwen3.7-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


async def main():
    # 异步调用一条请求
    response = await model.ainvoke("解释一下LangChain是什么，简洁回答100字以内")
    print(f"响应类型：{type(response)}")
    print(response.content_blocks)


# 4.运行异步函数
if __name__ == "__main__":
    asyncio.run(main())
