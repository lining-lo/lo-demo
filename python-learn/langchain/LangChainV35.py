"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc: LangChain+RedisStack 向量库基础增删改查与相似度检索
"""
# pip install langchain langchain-openai redis==5.3.1 langchain-core dashscope

import os
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis

# 初始化通义千问向量模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v3",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

# Redis配置常量
REDIS_URL = "redis://localhost:6379"
INDEX_NAME = "qwen_vector_index"
KEY_PREFIX = "qwen_doc:"

# 测试文档，携带完整元数据
texts = [
    "通义千问是阿里巴巴研发的大语言模型。",
    "Redis 是一个高性能的键值存储系统，支持向量检索。",
    "Milvus	开源的专为向量搜索设计的云原生数据库。性能强悍，功能丰富。覆盖轻量级的原型开发到十亿级向量的大规模生产系统",
    "LangChain 可以轻松集成各种大模型和向量数据库。"
]
documents = [
    Document(page_content=text, metadata={"source": "manual", "type": "tech"})
    for text in texts
]

def create_redis_store() -> Redis:
    vector_store = Redis.from_documents(
        documents=documents,
        embedding=embeddings,
        redis_url=REDIS_URL,
        index_name=INDEX_NAME,
        key_prefix=KEY_PREFIX
    )
    print("✅ 文档向量入库新增完成,共计插入文档记录条数：",len(documents))
    return vector_store

# 基础相似度检索
def simple_search(store: Redis, query: str, top_k=2):
    print(f"\n【基础相似检索】查询：{query}")
    res = store.similarity_search(query, k=top_k)
    for idx, doc in enumerate(res):
        print(f"结果{idx+1}: {doc.page_content} | 元数据:{doc.metadata}")
    return res

# 带相似度分值检索
def search_with_score(store: Redis, query: str, top_k=2):
    print(f"\n【带分值检索】查询：{query}")
    docs_score = store.similarity_search_with_score(query, k=top_k)
    for doc, score in docs_score:
        print(f"相似度:{score:.4f} 文本:{doc.page_content}")
    return docs_score

# 更新文档（先删后新增）
def update_demo(store: Redis):
    print("\n【更新文档演示,先删all后新增】")
    all_ids = store.client.keys(f"{KEY_PREFIX}*")
    if all_ids:
        store.delete(ids=all_ids)
    new_doc = Document(
        page_content="通义千问3 = qwen3.7-plus,是阿里新一代多模态大模型，支持图文、长文本理解",
        metadata={"source": "manual", "type": "llm"}
    )
    store.add_documents([new_doc])
    print("✅ 旧数据清空，写入更新文档，本次新增文档数量：1")
    ret = store.similarity_search("通义千问", k=1)
    print("更新后查询结果：", ret[0].page_content)

# 清空全部向量文档
def del_all(store: Redis):
    all_ids = store.client.keys(f"{KEY_PREFIX}*")
    if all_ids:
        store.delete(ids=all_ids)
        print(f"\n✅ 已删除全部 {len(all_ids)} 条文档")

if __name__ == "__main__":

    redis_vector = create_redis_store()

    simple_search(redis_vector, "什么是大语言模型")

    # search_with_score(redis_vector, "向量数据库有哪些")

    print()
    print("更新后查询=====================")
    update_demo(redis_vector)
    simple_search(redis_vector, "什么是大语言模型")
    print("更新后查询end=====================")

    del_all(redis_vector)

    empty_res = redis_vector.similarity_search("Redis", k=1)
    print("\n清空后检索到文档数量：", len(empty_res))