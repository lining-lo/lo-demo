"""
  @Author:lining-lo
  @Time:2026/9/3
  @Desc:skill使用
"""
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from day02.utils.llm_utils import get_llm_client

# 获取大模型实例
llm = get_llm_client()

# 创建深度智能体
deep_agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个高级智能助手，必须调用技能回答用户的问题",
    # 配置存储后端
    backend=FilesystemBackend(root_dir="../",virtual_mode=True),
    # 配置加载的技能
    skills=["skills"]
)

# 执行
result = deep_agent.invoke(
    input={
        "messages":[
            # {"role":"user","content":"列出所有的技能"}
            # {"role":"user","content":"将吴亦凡正在朝阳踩缝纫机转换为表情"}
            {"role":"user","content":"将🎤👨‍🎤🔒🚫🧵🪡🏭转换为中文"}
            # {"role":"user","content":"审查一下 11.技能.py 这个文件中的代码"}
        ]
    }
)
print(result)
# 打印输出结果
print(f"最终的结果是：{result['messages'][-1].content}")