"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:人机交互-处理
"""
import uuid
from deepagents import create_deep_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command
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
    system_prompt="你是一个高级智能管家",
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
    "configurable": {
        "thread_id": uuid.uuid4()
    }
}

# 第一次调用
result = deep_agent.invoke(
    input={
        "messages": [{"role": "user", "content": "请查询user_info表，然后再删除order_info表，最后删除main.txt文件"}]
    },
    # 设置配置信息
    config=config
)
print(f"第一次调用的结果是：{result['messages'][-1].content}")
# print(result["__interrupt__"])
# 创建一个决定列表
decisions = []
if result["__interrupt__"]:
    # 进行人工审批
    # 方式一：直接设置同意还是拒绝
    # decisions = [
    #     # 对于删除表的操作直接同意
    #     {"type":"approve"},
    #     # 对于删除文件的操作拒绝
    #     {"type":"reject"}
    # ]
    # 方式二：解析需要审批的结果
    # 获取需要审批的结果
    interrupt = result["__interrupt__"][0]
    # 获取action_requests
    action_requests = interrupt.value["action_requests"]
    if action_requests:
        # 遍历action_requests
        for action_request in action_requests:
            # 获取name
            name = action_request["name"]
            # 根据名字判断调用的是那个工具
            if name == "delete_table":
                # 设置删除表的审批结果
                decisions.append({"type": "approve"})
            if name == "delete_file":
                # 设置删除文件的审批结果
                # 拒绝删除文件
                # decisions.append({"type":"reject"})
                # 编辑删除文件
                decisions.append({
                    "type": "edit",
                    "edited_action": {
                        "name": name,  # 工具名称
                        "args": {"file_name": "test.txt"}  # 需要修改的参数
                    }
                })

    # 第二次调用
    result2 = deep_agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config
    )
    print(f"第二次调用的结果是：{result2['messages'][-1].content}")
