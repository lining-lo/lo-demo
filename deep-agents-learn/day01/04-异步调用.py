"""
  @Author:lining-lo
  @Time:2026/9/1
  @Desc:异步调用
"""
import asyncio
import json
import os
from deepagents import create_deep_agent
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

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    tools=[internet_search],
    system_prompt="你是一个超级智能助手，请调用工具回答用户的问题，字数控制在100字之内"
)

# 定义一个异步调用的函数
async def async_invoke(query: str):
    # 执行并流式输出
    result = deep_agent.astream(
        input={
            "messages":[{"role": "user", "content": query}]
        }
    )
    # 遍历
    async for chunk in result:
        # print(chunk)
        # 遍历获取每一个字典对象
        for key, value in chunk.items():
            # 判断是否是调用的模型
            if key == "model":
                # 获取AIMessage对象
                ai_message = value["messages"][-1]
                # 获取工具调用的列表
                tool_calls = ai_message.tool_calls
                # 判断是让调用工具还是最终输出结果
                if tool_calls:
                    # 遍历得到每一个工具
                    for tool_call in tool_calls:
                        # 获取工具的名称
                        tool_name = tool_call["name"]
                        # 获取调用工具时的参数
                        args = tool_call["args"]["query"]
                        print(f"智能体决定调用【{tool_name}】工具，传入的参数是：{args}")

                else:
                    # 获取最终的输出
                    final_output = ai_message.content
                    print(f"智能体最终的输出是：{final_output}")
            elif key == "tools":
                # 获取工具消息对象
                tool_message = value["messages"][-1]
                # 获取工具响应的内容
                content_str = tool_message.content
                # 将响应的内容转换为字典
                content_dict = json.loads(content_str)
                # 获取内容中的结果
                results = content_dict["results"]
                print(f"调用工具最终得到的结果是：{results}")
# 并发调用智能体的函数
async def main():
    as1 = async_invoke("LangChain是什么？")
    as2 = async_invoke("LangGraph是什么？")
    as3 = async_invoke("DeepAgents是什么？")
    await asyncio.gather(as1,as2,as3)

if __name__ == "__main__":
    # 并发调用智能体的函数
    asyncio.run(main())

