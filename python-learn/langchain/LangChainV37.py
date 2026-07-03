"""
  @Author:lining-lo
  @Time:2026/7/3
  @Desc:DML 数据写入（向量化 + 批量插入）
"""
# pip install pymilvus

from pymilvus import MilvusClient
from langchain_community.embeddings import DashScopeEmbeddings
import os

# 1. 连接 Milvus
client = MilvusClient("http://localhost:19530")

# 2. 初始化通义千问嵌入模型
embed_model = DashScopeEmbeddings(
    model="text-embedding-v3",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
)

# 3. 准备测试文本
texts = [
    "LangChain 是一个用于构建 LLM 应用的开发框架。",
    "Milvus 是一款高性能 AI 向量数据库。",
    "RAG 检索增强生成是大模型落地核心方案。",
    "Docker 可快速部署本地 Milvus 向量服务。"
]

# 4. 文本向量化
vectors = embed_model.embed_documents(texts)
print("向量数量：", len(vectors))
print("向量维度：", len(vectors[0]))

# 5. 封装 Milvus 可插入格式
data = [
    {
        "id": i,
        "vector": vectors[i],
        "text": texts[i],
        "source": "study_demo"
    }
    for i in range(len(texts))
]

# 6. 创建集合并写入数据
coll_name = "t_info"
client.create_collection(
    collection_name=coll_name,
    dimension=1024,
    metric_type="COSINE"
)

# 插入/更新数据
res = client.upsert(collection_name=coll_name, data=data)
print("写入结果：", res)

# 7. 手动 flush 落盘（内存数据刷入磁盘）
client.flush(collection_name=coll_name)

# 8. 查看集合数据统计
stats = client.get_collection_stats(collection_name=coll_name)
print("集合数据总量：", stats["row_count"])