"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:TypedDict使用案例
"""
import os
from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model

'''
LangChain也对这种能力提供了封装：不同厂商的模型都是继承了ChatModel基类，
而ChatModel提供了 with_structured_output方法，
传入pydantic base model类作为schema对象，得到一个新的llm对象，调用新的llm对象即可。
'''

llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

class Animal(TypedDict):
    animal: Annotated[str, "动物"]
    emoji: Annotated[str, "表情"]

class AnimalList(TypedDict):
    animals: Annotated[list[Animal], "动物与表情列表"] # List<Animal>

messages = [
    {"role": "user",
     "content": "任意生成三种动物，以及他们的 emoji 表情"}
]

llm_with_structured_output = llm.with_structured_output(AnimalList)
resp = llm_with_structured_output.invoke(messages)
print(resp)

