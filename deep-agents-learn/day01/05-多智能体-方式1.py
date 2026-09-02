"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:多智能体-方式1
"""
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

# 配置查询天气的子智能体
weather_agent = {
    "name": "weather_agent",
    "description": "查询天气的子智能体", # 该属性是给主智能体看的
    "system_prompt": "你是一个查询天气的智能助手",
    "tools": [internet_search]
}

# 计算助手的子智能体
math_agent = {
    "name": "math_agent",
    "description": "擅长数学计算的子智能体",
    "system_prompt": "你是一个数学天才，擅长各种数学计算"
}

# 翻译的子智能体
translate_agent = {
    "name": "translate_agent",
    "description": "翻译的子智能体",
    "system_prompt": "你是一个翻译天才，擅长各种语言的翻译"
}

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个智能体管家，请将任务分配给子智能体，同时让子智能体完成对应的任务",
    # 配置子智能体列表
    subagents=[weather_agent,math_agent,translate_agent]
)

# 执行并流式输出
result = deep_agent.stream(
    input={
        "messages":[{"role": "user", "content": "查询北京今天的天气，同时计算一下199+299等于多少，最后再将好好学习，天天向上翻译成日语"}]
    }
)
# 创建一个保存工具id和名字的字典
tool_dict = {}
# 遍历
for chunk in result:
    # print(chunk)
    # 遍历获取每一个字典对象
    for key,value in chunk.items():
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
                    args = tool_call["args"]["description"]
                    # 获取工具的id
                    tool_id = tool_call["id"]
                    # 保存工具id和名字
                    tool_dict[tool_id] = tool_name
                    print(f"智能体决定调用【{tool_name}】工具，传入的参数是：{args}")
            else:
                # 获取最终的输出
                final_output = ai_message.content
                print(f"智能体最终的输出是：{final_output}")
        elif key == "tools":
            # 获取工具消息对象
            tool_message = value["messages"][-1]
            # 获取工具响应的内容
            content = tool_message.content
            # 获取工具的id
            tool_id = tool_message.tool_call_id
            # 从字典中获取工具的名称
            tool_name = tool_dict[tool_id]
            print(f"【{tool_name}】工具返回的结果是：{content}")
