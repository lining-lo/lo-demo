"""
  @Author:lining-lo
  @Time:2026/9/3
  @Desc:长期记忆-memory
"""
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from day02.utils.llm_utils import get_llm_client

# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个高级智能助手",
    # 配置存储后端
    backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    # 配置长期记忆
    memory=["memories/AGENTS.md"],
)

# 执行
result = deep_agent.invoke(
    input={
        "messages": [
            {"role": "user", "content": "请记住，我叫罗志祥，我是时间管理大师"}
        ]
    }
)
print(result)
# 打印输出结果
print(f"最终的结果是：{result['messages'][-1].content}")
