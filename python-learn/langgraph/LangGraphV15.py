"""
  @Author:lining-lo
  @Time:2026/7/6
  @Desc:流式传输案例-自定义流式传输
"""

from typing import TypedDict
from langgraph.config import get_stream_writer
from langgraph.graph import StateGraph, START, END


# 定义图全局状态结构
class State(TypedDict):
    query: str  # 用户输入问题
    answer: str  # 模型回答结果


# 自定义业务节点
def node(state: State):
    # 获取流式写入器，用于推送自定义实时消息
    writer = get_stream_writer()
    # 推送一条自定义流式数据，只能被 stream_mode="custom" 捕获
    writer({"custom_key": "基泥苔煤，哦耶 O(∩_∩)O"})
    # 节点最终更新state里的answer字段
    return {"answer": "some data end"}


# 构建、编译流程图
graph = (
    StateGraph(State)
    .add_node("node", node)  # 注册自定义节点
    .add_edge(START, "node")  # 起始点指向业务节点
    .add_edge("node", END)  # 节点执行完直接结束
    .compile()
)

# 仅监听custom自定义流式消息
# 只会打印 writer 推送的自定义内容
for chunk in graph.stream({"query": "example"}, stream_mode=["custom"]):
    print(chunk)

print("*" * 40)

# 同时监听：state更新增量 + 自定义消息
# 输出两部分：字段变更内容、自定义推送文本
for chunk in graph.stream({"query": "example"}, stream_mode=["updates", "custom"]):
    print(chunk)

print("*" * 40)

# 同时监听：完整全局state + 自定义消息
# 输出两部分：每一步完整全部状态、自定义推送文本
for chunk in graph.stream({"query": "example"}, stream_mode=["values", "custom"]):
    print(chunk)
