"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:多智能体-方式3-兼容langgraph
"""
from typing import TypedDict, Annotated
from deepagents import CompiledSubAgent, create_deep_agent
from langchain_core.messages import AIMessage
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph
from utils.llm_utils import get_llm_client


# 定义状态
class State(TypedDict):
    messages: Annotated[list, add_messages]


# 定义节点函数
def call_llm(state: State):
    # 假设调用大模型，返回一个写死的数据
    return {"messages": [AIMessage(content="2030年世界杯举办地是：摩洛哥、葡萄牙、西班牙")]}


# 创建状态图实例
state_graph = StateGraph(state_schema=State)
# 添加节点
state_graph.add_node(call_llm)
# 添加边
# state_graph.set_entry_point("call_llm")
state_graph.add_edge(START, "call_llm")
state_graph.add_edge("call_llm", END)
# 编译
compiled_state_graph = state_graph.compile()

# 创建子智能体
sub_agent = CompiledSubAgent(
    name="兼容langgraph的子智能体",
    description="完成主智能体交给的任务，实现网络搜索",
    # 配置LangGraph编译之后的状态图实例
    runnable=compiled_state_graph
)

# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个智能体管家，所有任务都交给子智能体完成，你不要处理任何请求",
    subagents=[sub_agent]
)

# 执行
result = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "帮我查询一下2030年世界杯在哪儿举办"}
        ]
    }
)
print(result)
# 获取响应的内容
print(f"最终的响应内容是：{result['messages'][-1].content}")
