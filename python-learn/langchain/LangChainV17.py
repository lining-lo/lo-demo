"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:使用 from_messages 静态方法创建对话提示词模板
"""
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}，请回答我提出的问题"),
        ("human", "请回答:{question}")
    ]
)

prompt_value = chat_prompt.format_messages(role="老师", question="你的职业和特长")
print(prompt_value)

result = model.invoke(prompt_value)
print(result.content)
