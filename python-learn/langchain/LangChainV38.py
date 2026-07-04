"""
  @Author:lining-lo
  @Time:2026/7/3
  @Desc:DQL 数据查询（遍历 + 主键查询 + 相似度检索）
"""
from pymilvus import MilvusClient
from langchain_community.embeddings import DashScopeEmbeddings
import os

# 1. 连接客户端、加载模型
client = MilvusClient("http://localhost:19530")
embed_model = DashScopeEmbeddings(
    model="text-embedding-v3",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
)

# 2. 全量遍历所有数据
print("===== 全量数据遍历 =====")
coll_name = "t_info"
iterator = client.query_iterator(
    collection_name=coll_name,
    filter="",
    output_fields=["*"]
)
idx = 1
while True:
    rows = iterator.next()
    if not rows:
        break
    for row in rows:
        print(f"第{idx}条：id={row['id']}, text={row['text']}")
        idx += 1
iterator.close()

# 3. 根据主键 ID 精准查询
print("\n===== 主键精准查询 =====")
res = client.get(collection_name=coll_name, ids=[0, 1])
for item in res:
    print(item)

# 3. 相似度向量检索（RAG核心）
print("\n===== 向量相似度检索 =====")
query = "什么是向量数据库？"
query_vec = embed_model.embed_query(query)

search_res = client.search(
    collection_name=coll_name,
    data=[query_vec],
    limit=3,
    output_fields=["text", "source"]
)

for item in search_res[0]:
    print(f"相似度分数：{item['distance']:.4f} | 内容：{item['entity']['text']}")
