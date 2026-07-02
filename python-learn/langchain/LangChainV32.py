"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc:文本向量化入门案例_OpenAI 兼容写法2
"""
import os
from langchain_openai import OpenAIEmbeddings

# 阿里云通义向量兼容OpenAI配置
embeddings = OpenAIEmbeddings(
    model="text-embedding-v4",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    # 关闭长度校验，适配阿里云向量接口规则
    check_embedding_ctx_length=False
)

# 单文本向量化
text = "This is a test document."
query_result = embeddings.embed_query(text)
print("文本向量长度：", len(query_result), sep='')

# 批量文档向量化
doc_list = [
    "Hi there!",
    "Oh, hello!",
    "What's your name?",
    "My friends call me World",
    "Hello World!"
]
doc_results = embeddings.embed_documents(doc_list)

print(doc_results)
print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')