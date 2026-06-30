"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:接入deepseek
"""
# 1.导入依赖
import os
from langchain_deepseek import ChatDeepSeek

# 2.实例化模型
model = ChatDeepSeek(
    model="deepseek-v4-pro",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 打印结果
print(model.invoke("你是谁").content)
