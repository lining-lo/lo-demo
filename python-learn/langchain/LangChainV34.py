"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc:LangChain 结合 RedisStack 实现向量存储与 RAG 检索案例
"""
# pip install langchain-community dashscope redis==5.3.1

import os
# 阿里云通义向量
from langchain_community.embeddings import DashScopeEmbeddings
# Redis向量库
from langchain_community.vectorstores import Redis
from langchain_core.documents import Document

# 1. 初始化阿里千问 Embedding 模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v3",  # 支持 v1 或 v2
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")  # 从环境变量读取
)

# 2. 准备要向量化的文本（Document 列表）
texts = [
    "通义千问是阿里巴巴研发的大语言模型。",
    "Redis 是一个分布式内存数据库，也可以作为一种向量数据库。",
    "LangChain 与其他组件连接成链，可以轻松集成各种大模型借此构建AI工程应用"
]
documents = [Document(page_content=text, metadata={"source": "manual"}) for text in texts]

# 3. 连接到 Redis 并存入向量（自动调用 embeddings 嵌入）
vector_store = Redis.from_documents(
    documents=documents,
    embedding=embeddings,
    redis_url="redis://localhost:6379",  # 替换为你的 Redis 地址
    index_name="my_index11",  # 向量索引名称
)

# 4. 将 Redis 向量库转为通用检索器，每次检索固定返回相似度最高 1 条文档，用于 RAG 检索流程。
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

# 5. 打印
results = retriever.invoke("LangChain是什么？")
for res in results:
    print(res.page_content)
