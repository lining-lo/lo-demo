"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc:文本向量化入门案例_阿里云官方写法
"""
# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587
import os

import dashscope
from http import HTTPStatus

input_text = "衣服的质量杠杠的"
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")  # 从环境变量读取

resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",
    input=input_text,
)

if resp.status_code == HTTPStatus.OK:
    print(resp)