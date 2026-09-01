"""
  @Author:lining-lo
  @Time:2026/9/1
  @Desc:使用LangSmith监控流程
"""
import os
from typing import Literal
from deepagents import create_deep_agent
from dotenv import load_dotenv
from tavily import TavilyClient
from utils.llm_utils import get_llm_client

# 加载.env文件
load_dotenv()

# LangSmith追踪配置
os.environ.setdefault("LANGSMITH_API_KEY", os.getenv("LANSMITH_API_KEY"))
# os.environ.setdefault("LANGSMITH_TRACING", "true")
# os.environ.setdefault("LANGSMITH_PROJECT", "deep‑agents‑learn")

# 创建Tavily客户端
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def internet_search(
        query: str,
        max_results: int = 2,
        topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = False,
):
    """
    Tavily网络搜索工具方法
    :param query: 要查询的内容
    :param max_results: 返回的结果数量
    :param topic: 主题
    :param include_raw_content: 是否包含原始内容
    :return:
    """
    print("调用Tavigy网络搜索工具")
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# 创建大模型实例
llm = get_llm_client()

# 创建深度智能体实例
agent = create_deep_agent(
    # 配置使用的模型
    model=llm,
    # 配置工具列表
    tools=[internet_search],
    # 配置系统提示词
    system_prompt="你是一个智能助手，有必要时可以调用工具回答用户的问题"
)
# 执行
result = agent.invoke(
    input={
        "messages": [{"role": "user", "content": "帮我查询一下牛来最新的票房"}]
    }
)
# print(result)
# 获取响应的内容
print(result["messages"][-1].content)
