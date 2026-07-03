"""
  @Author:lining-lo
  @Time:2026/7/3
  @Desc:DDL 结构管理（数据库、集合创建与删除）
"""
#  pip install pymilvus

# 导入客户端、连接 Milvus
from pymilvus import MilvusClient

# 连接本地 Milvus v2.5.5
client = MilvusClient("http://localhost:19530")

# ===================== 1. 查看所有数据库 =====================
db_list = client.list_databases()
print("所有数据库：", db_list)

# ===================== 2. 创建数据库（防重复报错） =====================
db_name = "rag_study_demo"
if db_name not in db_list:
    client.create_database(db_name)
    print(f"数据库 {db_name} 创建成功")
else:
    print(f"数据库 {db_name} 已存在")

# ===================== 3. 切换数据库 =====================
client.use_database(db_name)
print(f"已切换至数据库：{db_name}")

# ===================== 4. 创建集合 Collection =====================
coll_name = "study_info"
client.create_collection(
    collection_name=coll_name,
    dimension=1024,
    metric_type="COSINE"
)
print(f"集合 {coll_name} 创建成功")

# ===================== 5. 查看当前库所有集合 =====================
coll_list = client.list_collections()
print("当前库所有集合：", coll_list)

# ===================== 6. 删除集合 =====================
client.drop_collection(coll_name)
print(f"集合 {coll_name} 已删除")

# ===================== 7. 删除数据库（需先删集合） =====================
client.drop_database(db_name)
print(f"数据库 {db_name} 已删除")
