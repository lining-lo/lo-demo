"""
  @Author:lining-lo
  @Time:2026/7/5
  @Desc:LangGraph入门案例1-基础案例
"""
# pip install grandalf

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import uuid


# 1．定义State对象
class HelloState(TypedDict):
    name: str
    greeting: str


# 2.定义节点Node(就是干活的函数)
def greet(helloState: HelloState) -> dict:
    name = helloState["name"]
    return {"greeting": f"你好,{name}"}
    # return helloState


def add_emoji(helloState: HelloState) -> dict:
    greeting = helloState["greeting"]
    return {"greeting": greeting + "  。。。😄"}


# 3.构建图graph
graph = StateGraph(HelloState)

graph.add_node("greeting", greet)
graph.add_node("add_emoji", add_emoji)

graph.add_edge(START, "greeting")
graph.add_edge("greeting", "add_emoji")
graph.add_edge("add_emoji", END)

# 4.编译图
app = graph.compile()

# 5.运行
# invoke()方法只接收状态字典作为核心参数
result = app.invoke({"name": "z3"})
print(result)
print()
print(result["greeting"])

# 6 打印图的边和节点信息
# 6.1 打印图的ascii可视化结构
print(app.get_graph().print_ascii())
print("=" * 50)

# 6.2 打印图的Mermaid代码可视化结构并通过https://www.processon.com/mermaid编辑器查看
print(app.get_graph().draw_mermaid())
print("=" * 50)

# 6.3 生成 PNG并写入文件 ，一般需要开启科学上网
png_bytes = app.get_graph().draw_mermaid_png(max_retries=2, retry_delay=2.0)
output_path = "langgraph" + str(uuid.uuid4())[:8] + ".png"
with open(output_path, "wb") as f:
    f.write(png_bytes)
print(f"图片已生成：{output_path}")
