"""
  @Author:lining-lo
  @Time:2026/9/3
  @Desc:
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载.env文件
load_dotenv()


# 定义一个返回大模型实例的函数
def get_llm_client():
    return ChatOpenAI(
        model=os.getenv("ALIYUN_MODEL"),
        api_key=os.environ["DASHSCOPE_API_KEY"],
        base_url=os.getenv("ALIYUN_BASE_URL")
    )
