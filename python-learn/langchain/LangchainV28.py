"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc:文本向量化入门案例_OpenAI 兼容写法1
"""
# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587
import os
from openai import OpenAI

input_text = "衣服的质量杠杠的"

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

completion = client.embeddings.create(
    model="text-embedding-v4",
    input=input_text
)

print(completion.model_dump_json())
