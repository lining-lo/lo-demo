"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:子智能体的格式化输出
"""
import os
from deepagents import create_deep_agent
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from tavily import TavilyClient
from day02.utils.llm_utils import get_llm_client

# 创建Tavily客户端对象
tavily_client = TavilyClient(
    api_key=os.environ["TAVILY_API_KEY"]
)

@tool(description="网络搜索的工具")
def internet_search(query: str):
    return tavily_client.search(query)

# 定义一个格式化输出的类
class PrettyGirl(BaseModel):
    name: str = Field(description="名字")
    dynasty: str = Field(description="朝代")
    title: str = Field(description="称号")
    introduction: str = Field(description="简介")

class ResearchFindings(BaseModel):
    """Structured findings from a research task."""
    summary: str = Field(description="Summary of findings")
    confidence: float = Field(description="Confidence score from 0 to 1")
    sources: list[str] = Field(description="List of source URLs")

# 自定义输出数据格式的类型
class WeatherResponse(BaseModel):
    city: str = Field(description="城市名称")
    temperature: int = Field(description="温度")
    condition: str = Field(description="天气状况")

# 创建子智能体
sub_agent = {
    "name": "网络搜索的子智能体",
    "description": "我是一个网络搜索助手，上知天文，下知地理",
    "system_prompt":"你是一个智能助手，请调用网络搜索工具完成功能，并按照response_format指定的格式输出，不要自由发挥",
    "tools":[internet_search],
    # 配置格式化输出
    "response_format": WeatherResponse
}

# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    name="深度智能体",
    model=llm,
    system_prompt="你是一个强大的管家，不要自己处理任务，将任务交给子智能体完成",
    subagents=[sub_agent]
)

# 执行
result = deep_agent.invoke(
    input={
        # "messages":[{"role":"user","content":"北京今天的天气怎么样，以json格式输出"}]
        "messages":[{"role":"user","content":"中国历史上唯一的女皇帝是谁"}]
        # "messages": [{"role": "user", "content": "Research recent advances in quantum computing"}]
    }
)
# 获取最终的结果
print(f"最终的结果是：{result['messages'][-1].content}")