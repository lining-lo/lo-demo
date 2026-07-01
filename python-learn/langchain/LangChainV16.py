"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:使用使用构造方法创建对话提示词模板
"""
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# tuple 构成的列表，格式为[(role, content)]
chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

prompt = chatPromptTemplate.format_messages(
    name="小狸AI", thing="AI", user_input="7 + 5等于多少"
    )
print(prompt)

result = model.invoke(prompt)
print(result.content)