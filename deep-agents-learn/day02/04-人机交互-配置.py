"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:人机交互-配置
"""
import uuid
from deepagents import create_deep_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from day02.utils.llm_utils import get_llm_client


# 定义工具函数
@tool(description="根据表名查询表中的数据")
def query_table(table_name: str):
    print(f"调用了【query_table】工具")
    return f"查询了【{table_name}】表中的数据"


@tool(description="根据表名删除表中的数据")
def delete_table(table_name: str):
    print(f"调用了【delete_table】工具")
    return f"删除了【{table_name}】表中的数据"


@tool(description="根据文件名删除文件")
def delete_file(file_name: str):
    print(f"调用了【delete_file】工具")
    return f"删除了【{file_name}】文件"


# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    name="人机交互",
    system_prompt="你是一个高级智能管家，你需要根据用户的指令，调用对应的工具函数，并返回结果",
    tools=[query_table, delete_table, delete_file],
    # 配置人机交互
    interrupt_on={
        "query_table": False,  # 不需要审核
        "delete_table": True,  # 需要审核，审核类型有：approve、reject、edit、response
        "delete_file": {
            "allowed_decisions": ["approve", "edit", "reject"]
        }
    },
    # 处理配置人机交互，还需要配置检查点
    checkpointer=MemorySaver()
)

# 创建配置
config = {
    "configurable":{
        "thread_id": uuid.uuid4()
    }
}

# 执行
result = deep_agent.invoke(
    input={
        "messages": [{"role": "user", "content": "请查询user_info表，然后再删除order_info表，最后删除test.txt文件"}]
    },
    # 设置配置信息
    config=config
)
print(result)
print(f"最终的结果是：{result['messages'][-1].content}")
