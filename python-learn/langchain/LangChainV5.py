"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:以ChatOpenAI的方式接入OpenAI
"""
# 1.导入依赖
import os
from langchain_openai import ChatOpenAI

# 2.实例化模型
model = ChatOpenAI(
    model="qwen3.7-max",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 3.调用模型
print(model.invoke("你是谁").content)
