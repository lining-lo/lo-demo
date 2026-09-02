"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:多智能体-方式二-兼容langchain
"""
import os
from deepagents import CompiledSubAgent, create_deep_agent
from langchain.agents import create_agent
from langchain_core.tools import tool
from tavily import TavilyClient
from utils.llm_utils import get_llm_client

# 创建Tavily客户端
tavily_client = TavilyClient(
    api_key=os.environ["TAVILY_API_KEY"]
)

# 定义搜索函数
@tool(description="网络搜索工具")
def internet_search(query: str):
    # 调用Tavily客户端的search方法
    return tavily_client.search(query)

# 获取大模型实例
llm = get_llm_client()

# 通过langchai创建一个智能体作为深度智能体的子智能体
agent = create_agent(
    model=llm,
    tools=[internet_search]
)

# 创建子智能体
sub_agent = CompiledSubAgent(
    name="兼容langchain的子智能体",
    description="完成主智能体交给的任务，实现网络搜索",
    runnable=agent
)

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个智能体管家，请将任务交给子智能体完成",
    subagents=[sub_agent]
)

# 执行
result = deep_agent.invoke(
    input={
        "messages":[
            {"role":"user","content":"帮我查询一下2030年世界杯在哪儿举办"}
        ]
    }
)
# 获取响应的内容
print(f"最终的响应内容是：{result['messages'][-1].content}")