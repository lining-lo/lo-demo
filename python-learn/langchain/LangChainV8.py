"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:同步普通调用_invoke
"""
# 1.导入依赖
import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

# 2.实例化模型
model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 构建消息列表
messages = [
    SystemMessage(content="你是一个法律助手，只回答法律问题，超出范围的统一回答，非法律问题无可奉告"),
    # HumanMessage(content="简单介绍下广告法，一句话告知50字以内")
    HumanMessage(content="2+3等于几?")
]

# 3.调用模型
response = model.invoke(messages)
print(f"响应类型：{type(response)}")
# 打印结果
print(response.content)
print(response.content_blocks)
