"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:angchain入门案例2-接入Deepseek大模型
"""
# 1.导入依赖
import os
from langchain.chat_models import init_chat_model

# 2.实例化模型
model = init_chat_model(
    model="qwen3.7-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"), #配置在自己本地环境变量里
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 3.调用模型
print(model.invoke("你是谁，50字内回复"))
