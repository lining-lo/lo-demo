"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:外部加载_JSON
"""

import json
from langchain_core.prompts import PromptTemplate

# 读取prompt配置
with open("prompt.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 手动实例化PromptTemplate，完全规避beta序列化接口
template = PromptTemplate(
    input_variables=data["input_variables"],
    template=data["template"]
)

res = template.format(name="张三", what="搞笑的")
print(res)