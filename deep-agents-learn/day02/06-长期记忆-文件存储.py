"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:长期记忆-文件存储
"""
import os
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langchain_core.tools import tool
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

# 创建深度智能体
deep_agent = create_deep_agent(
    name="测试文件存储",
    model=llm,
    system_prompt="你是一个高级智能助手，请根据用户的指令读写文件",
    tools=[internet_search],
    # root_dir：配置文件存储的根目录 virtual_mode：是否开启虚拟模式，如果不开启，配置的根目录将形同虚设
    backend=FilesystemBackend(root_dir="temp_data", virtual_mode=True),
)

# 执行
result = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "帮我查询一下北京大学信息并保存到根目录下的test.txt文件中"}
        ]
    }
)

# 打印结果
print(f"最终的结果是：{result['messages'][-1].content}")
