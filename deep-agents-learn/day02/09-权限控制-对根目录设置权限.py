"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:权限控制-对根目录设置权限
"""
from deepagents import create_deep_agent, FilesystemPermission
from deepagents.backends import FilesystemBackend
from day02.utils.llm_utils import get_llm_client

# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    name="权限控制-对根目录设置权限",
    model=llm,
    system_prompt="""
        你是一个高级智能助手
    """,
    # 配置存储后端为文件存储
    backend=FilesystemBackend(root_dir="temp_data", virtual_mode=True),
    # 配置工作目录的权限
    permissions=[
        FilesystemPermission(
            # 配置权限
            operations=["write"],
            paths=["/**"],
            # 配置模式为拒绝
            mode="deny",
        ),
    ]
)

# 第一次执行：测试读取权限-允许
result = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "读取local.txt中的内容"}
        ]
    },
    config={
        "configurable": {"thread_id": "thread_id_9527"}
    }
)
# 打印结果
print(f"第一次执行的结果是：{result['messages'][-1].content}")
print("=" * 88)
# 第二次执行：测试写的权限-拒绝
result2 = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "在根目录创建lzx.txt文件，内容是：我叫罗志祥，我是时间管理大师"}
        ]
    },
    config={
        "configurable": {"thread_id": "thread_id_9528"}
    }
)
# 打印结果
print(f"第二次执行的结果是：{result2['messages'][-1].content}")
