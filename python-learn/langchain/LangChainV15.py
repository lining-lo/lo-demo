"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:使用 from_template 静态方法创建提示词模板
"""
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，"
                                        "我的问题是：{question}")

prompt = template.format(role="python开发", question="快速排序怎么写？")
print(prompt)

result = model.invoke(prompt)
print(result.content)
