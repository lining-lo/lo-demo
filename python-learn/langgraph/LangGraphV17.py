"""
  @Author:lining-lo
  @Time:2026/7/7
  @Desc:普通边案例
"""
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


# 定义状态
class GraphState(TypedDict):
    value: int
    step: str


# 定义节点函数
def node_a(state: GraphState) -> dict:
    """节点A"""
    print("执行节点A")
    return {"value": state["value"] + 1, "step": "A执行完毕"}


def node_b(state: GraphState) -> dict:
    """节点B"""
    print("执行节点B")
    return {"value": state["value"] * 2, "step": "B执行完毕"}


def node_c(state: GraphState) -> dict:
    """节点C"""
    print("执行节点C")
    return {"value": state["value"] - 1, "step": "C执行完毕"}


def main():
    # 创建图
    builder = StateGraph(GraphState)

    # 添加节点
    builder.add_node("node_a", node_a)
    builder.add_node("node_b", node_b)
    builder.add_node("node_c", node_c)

    # 添加普通边
    builder.add_edge(START, "node_a")  # 从开始到A
    builder.add_edge("node_a", "node_b")  # 从A到B
    builder.add_edge("node_b", "node_c")  # 从B到C
    builder.add_edge("node_c", END)  # 从C到结束

    # 编译图
    app = builder.compile()

    # 执行图
    result = app.invoke({"value": 1})
    print(f"执行结果: {result}\n")
    # 打印图的边和节点信息
    print(builder.edges)
    print(builder.nodes)
    # 打印图的ascii可视化结构
    print(app.get_graph().print_ascii())


if __name__ == "__main__":
    main()
