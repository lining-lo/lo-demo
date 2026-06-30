"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:langchain入门案例1-接入阿里百炼平台的通义模型
"""
# 1.导入依赖
import os
from langchain.chat_models import init_chat_model

# 2.实例化模型
model = init_chat_model(
    model="deepseek-v4-pro",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"), #配置在自己本地环境变量里
    base_url="https://api.deepseek.com"
)

# 3.调用模型
print(model.invoke("你是谁，50字内回复"))
