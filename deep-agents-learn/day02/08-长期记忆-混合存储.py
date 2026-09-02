"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:长期记忆-混合存储
"""
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend, StoreBackend, store, CompositeBackend
from langgraph.store.memory import InMemoryStore
from utils.llm_utils import get_llm_client

# 获取大模型实例
llm = get_llm_client()

# 创建内存存储存储后端
store = InMemoryStore()

# 创建深度智能体
deep_agent = create_deep_agent(
    name="测试混合存储",
    model=llm,
    system_prompt="""
        你是一个高级智能助手，请按照以下要求存储数据：
        -重要文件：存储到指定的工作目录中
        -普通文件：存储到指定的内存中
    """,
    # 配置存储后端为混合存储
    backend=CompositeBackend(
        # 配置默认的存储方式为文件存储
        default=FilesystemBackend(root_dir="../temp_data",virtual_mode=True),
        # 对于内存存储配置了路由，当存储的路径以/memories开头时将存储到内存中
        routes={
            "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
        },
    ),
    store=store
)

# 第一次执行
result = deep_agent.invoke(
    input={
        "messages":[
            {"role":"user","content":"帮我执行以下内容：1、创建一个local.txt文件，内容是：我叫蔡徐坤，我喜欢打篮球、唱歌、Rap。2、向/memories/user.txt文件中写入：我叫吴亦凡，我正在踩缝纫机"}
        ]
    },
    config={
        "configurable":{"thread_id":"thread_id_9527"}
    }
)
# 打印结果
print(f"第一次执行的结果是：{result['messages'][-1].content}")
print("="*88)
# 第二次执行：查询文件中的内容
result2 = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "查询local.txt中的内容"}
        ]
    },
    config={
        "configurable": {"thread_id": "thread_id_9528"}
    }
)
# 打印结果
print(f"第二次执行的结果是：{result2['messages'][-1].content}")
print("="*88)
# 第二次执行：查询文件中的内容
result3 = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "查询/memories/user.txt文件中中的内容"}
        ]
    },
    config={
        "configurable": {"thread_id": "thread_id_9529"}
    }
)
# 打印结果
print(f"第三次执行的结果是：{result3['messages'][-1].content}")

