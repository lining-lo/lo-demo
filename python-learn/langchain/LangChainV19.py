"""
  @Author:lining-lo
  @Time:2026/7/1
  @Desc:外部加载_YAML
"""
from langchain_core.prompts import load_prompt

template = load_prompt("prompt.yaml", encoding="utf-8")
print(template.format(name="年轻人", what="滑稽"))
# 请年轻人讲一个滑稽的故事

#
# import yaml
# from langchain_core.prompts import PromptTemplate
#
# # 读取yaml文件，指定utf-8编码
# with open("prompt.yaml", "r", encoding="utf-8") as f:
#     prompt_config = yaml.safe_load(f)
#
# # 手动实例化标准PromptTemplate对象，彻底规避不稳定序列化接口
# prompt_template = PromptTemplate(
#     input_variables=prompt_config["input_variables"],
#     template=prompt_config["template"]
# )
# # 填充变量并打印结果
# result = prompt_template.format(name="年轻人", what="滑稽")
# print(result)
#