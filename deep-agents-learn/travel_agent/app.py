"""
  @Author:lining-lo
  @Time:2026/9/3
  @Desc: 
"""
import asyncio
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from travel_agent.core.map_agent import map_agent
from travel_agent.core.ticket_agent import ticket_agent
from travel_agent.utils.llm_utils import get_llm_client

MAIN_AGENT_PROMPT = """
你是一名旅游规划总控智能体。
你的职责是根据用户输入，先抽取关键信息，再调度合适的子智能体完成任务。

规则：
1. 先从用户输入中抽取：出发地、目的地、日期/天数、预算、偏好、出行节奏
2. 如果用户没有明确说明游玩天数，默认按 1 天规划
3. 如果用户没有明确说明预算，默认按中等预算规划
4. 如果用户没有明确说明偏好，默认按“经典景点 + 少折腾”规划
5. 如果用户没有明确说明出行节奏，默认按“舒适型节奏”规划
6. 景点、路线、地图相关问题交给 map_agent
7. 火车票、车次、票价、时间建议交给 ticket_agent
8. 最终结果交给 summary_agent 汇总
9. 输出必须使用中文
10. 不做真实购票，只做规划和建议
"""

# 获取大模型实例
llm = get_llm_client()

# 创建主智能体
main_agent = create_deep_agent(
    name="旅游规划助手",
    model=llm,
    system_prompt=MAIN_AGENT_PROMPT,
    # 配置存储后端
    backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    # 配置长期记忆
    memory=["/memory/AGENTS.md"],
    # 配置子智能体
    subagents=[ticket_agent]
)

async def main():
    result = await main_agent.ainvoke(
        input={
            "messages": [
                {"role": "user", "content": "帮我查询一下北京到濮阳东的高铁"}
            ]
        }
    )
    print(result['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
