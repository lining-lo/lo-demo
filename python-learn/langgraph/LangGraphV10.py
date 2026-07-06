"""
  @Author:lining-lo
  @Time:2026/7/6
  @Desc:Reducers规约函数-自定义乘法Reducer
"""
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


# 自定义乘法规约函数
def MyOperatorMul(current: float | None, update: float) -> float:
    """
    current：当前存量值（首次为 0）
    update：节点本次更新传入的值
    返回：新旧相乘结果
    """
    # 第一次更新，无历史值，直接使用update
    if current == 0:
        print(f"首次更新，无历史值，直接赋值：update={update}")
        return update
    # 已有历史值，执行乘法
    print(f"历史值current={current}，本次更新update={update}，相乘结果={current * update}")
    return current * update


class MultiplyState(TypedDict):
    factor: Annotated[float, MyOperatorMul]


# 节点：每次返回乘以2的增量更新
def multiplier(state: MultiplyState) -> dict:
    return {"factor": 2.0}


def run_demo():
    builder = StateGraph(MultiplyState)
    builder.add_node("multiplier", multiplier)
    builder.add_edge(START, "multiplier")
    builder.add_edge("multiplier", END)

    graph = builder.compile()

    # 初始传入5.0，节点会循环两次 *2
    result = graph.invoke({"factor": 5.0})
    print(f"\n初始输入: {{'factor': 5.0}}")
    print(f"最终结果: {result}")
    # 流程：5 → 5*2=10 输出 factor=10


if __name__ == "__main__":
    run_demo()
