"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:Model I/O的参数
"""
import os
from langchain.chat_models import init_chat_model

# ====================== 1. 初始化必填参数（缺一不可） ======================
chat_model = init_chat_model(
    # 必填1：模型名称
    model="deepseek-v4-pro",
    # 必填2：接口协议类型，兼容OpenAI统一填openai
    model_provider="openai",
    # 必填3：密钥，读取系统环境变量
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    # 必填4：厂商接口地址
    base_url="https://api.deepseek.com",

    # ====================== 2. 生成控制可调参数（按需修改） ======================
    temperature=0.1,  # 低随机性，适合写代码、专业问答
    max_tokens=1024,  # 限制最大输出长度
    top_p=0.3,  # 只选用高概率文字，回答严谨
    frequency_penalty=0.2,  # 减少语句重复
    stop=["结束回答"]  # 遇到指定文字立刻停止生成
)

# 调用测试
res = chat_model.invoke("写一段读取环境变量的Python代码")
print(res.content)
