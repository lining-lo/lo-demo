"""
  @Author:lining-lo
  @Time:2026/6/30
  @Desc:进阶案例-同时存在多种大模型产品在系统里共存使用
"""

import os
from langchain.chat_models import init_chat_model

# ══════════════════════════════════════════════════════
# 1. 实例化两个模型（不同供应商）
# ══════════════════════════════════════════════════════

# —— 1a. 阿里云通义千问 qwen3.7-max ——
# 通过 OpenAI 兼容协议访问阿里云 DashScope 接入点
llm_qwen = init_chat_model(
    model="qwen3.7-max",  # 通义千问最新旗舰模型
    model_provider="openai",  # 使用 OpenAI 兼容接口
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 密钥存本地环境变量
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里云接入点
    temperature=0,
)

# —— 1b. DeepSeek V4 Pro ——
# 通过 OpenAI 兼容协议访问 DeepSeek 官方 API
llm_deepseek = init_chat_model(
    model="deepseek-v4-pro",  # DeepSeek 第四代旗舰
    model_provider="openai",  # DeepSeek 同样兼容 OpenAI 协议
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从环境变量配置中读取
    base_url="https://api.deepseek.com",  # DeepSeek 官方 API 地址
    temperature=0,
)

# ══════════════════════════════════════════════════════
# 2. 分别调用两个模型
# ══════════════════════════════════════════════════════

prompt = "你是谁，50字内回复"

print("=" * 60)
print("🤖 通义千问 qwen3.7-max 回复：")
resp_qwen = llm_qwen.invoke(prompt)
print(resp_qwen.content)

print("=" * 60)
print("🤖 DeepSeek V4 Pro 回复：")
resp_deepseek = llm_deepseek.invoke(prompt)
print(resp_deepseek.content)

print("=" * 60)
