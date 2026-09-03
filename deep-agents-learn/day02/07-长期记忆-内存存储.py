"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:长期记忆-内存存储
"""
import os
from deepagents import create_deep_agent
from deepagents.backends import StoreBackend
from langchain_core.tools import tool
from langgraph.store.memory import InMemoryStore
from tavily import TavilyClient
from day02.utils.llm_utils import get_llm_client

# 创建Tavily客户端对象
tavily_client = TavilyClient(
    api_key=os.environ["TAVILY_API_KEY"]
)

@tool(description="网络搜索的工具")
def internet_search(query: str):
    return tavily_client.search(query)

# 获取大模型实例
llm = get_llm_client()

# 创建内存存储存储后端
store = InMemoryStore()

# 创建深度智能体
deep_agent = create_deep_agent(
    name="测试内存存储",
    model=llm,
    system_prompt="你是一个高级智能助手，请将用户的信息保存到user_info.txt文件中，同时也可以通过user_info.txt文件获取用户的信息",
    tools=[internet_search],
    # 配置长期记忆存储的方式
    backend=StoreBackend(
        namespace=lambda _: ("thread_id_9527",)
    ),
    # 配置内存存储，存储的是Key:Value的形式
    store=store
)

# 第一次执行
result = deep_agent.invoke(
    input={
        "messages":[
            {"role":"user","content":"我叫蔡徐坤，我喜欢打篮球"}
        ]
    },
    config={
        "configurable":{"thread_id":"thread_id_9527"}
    }
)
# 打印结果
print(f"第一次执行的结果是：{result['messages'][-1].content}")
# 手动查询结果
store_result = store.search(("thread_id_9527",))
print(f"手动查询的结果是：{store_result}")
print("="*88)
# 第二次执行
result2 = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "我叫什么，我的爱好是什么"}
        ]
    },
    config={
        "configurable": {"thread_id": "thread_id_8888"}
    }
)
# 打印结果
print(f"第二次执行的结果是：{result2['messages'][-1].content}")

