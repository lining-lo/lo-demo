"""
  @Author:lining-lo
  @Time:2026/9/2
  @Desc:子智能体嵌套-CompiledSubAgent
"""
from dotenv import load_dotenv
from deepagents import (CompiledSubAgent, create_deep_agent)
from day02.utils.llm_utils import get_llm_client

# 加载.env配置
load_dotenv()

# 初始化model
chat_model = get_llm_client()

# 底层coder配置
# 职责明确：只有他能写代码
coder_agent = create_deep_agent(
    model=chat_model,
    tools=[],
    subagents=[],
    name="CODER",
    system_prompt="""
你是 CODER，高级 Python 工程师。

职责边界：
1. 你只负责直接写代码。
2. 不要再继续分派任务。
3. 输出最终答案时，直接给出可运行的 Python 代码字符串。
4. 除代码外，只允许加极少量必要说明。
        """.strip(),
)

# 中间层CTO配置
# 职责明确：承上启下，必须指挥coder
coder_subagent = CompiledSubAgent(
    name="coder",
    description="负责编写 Python 代码。所有实际编码任务都必须交给它。",
    runnable=coder_agent,
)
cto_agent = create_deep_agent(
    model=chat_model,
    tools=[],
    subagents=[coder_subagent],
    name="CTO",
    system_prompt="""
你是 CTO，技术负责人。

职责边界：
1. 你负责理解 CEO 下发的需求，并拆解成具体编码任务。
2. 你不能亲自写代码。
3. 只要任务涉及编写 Python 代码，必须调用 coder 子代理。
4. 你的最终输出应当是 coder 返回的代码结果，不要自行改写为伪代码。
        """.strip(),
)

# 顶层CEO配置
# 职责明确：只负责战略，禁止干具体的活
cto_subagent = CompiledSubAgent(
    name="cto",
    description="不要亲自生成代码，必须调用子代理完成编码。",
    runnable=cto_agent,
)
ceo_agent = create_deep_agent(
    model=chat_model,
    name="CEO",
    # 关键修改：明确告诉CEO不要自己动手，必须找CTO
    system_prompt="""
        你是CEO，负责公司战略决策。
        注意：你严禁直接编写代码或操作文件！
        你必须将所有技术相关的开发任务委派给 'CTO' 处理。
        你的工作是验收 CTO 提交的结果。
    """,
    subagents=[cto_subagent]
)

print(">>>开始执行任务...")
stream = ceo_agent.stream(
    {
        "messages": [
            {"role": "user", "content": "使用python实现冒泡排序，只用生成代码字符串即可！！"}
        ]
    },
    # subgraphs=True  #让 stream() 把“子图/子代理内部”的事件也一起流出来，而不只给你最外层主图的事件。
)

print("\n>>> 最终结果：")
for chunk in stream:
    print(chunk)
