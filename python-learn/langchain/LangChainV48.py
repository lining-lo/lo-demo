"""
  @Author:lining-lo
  @Time:2026/7/5
  @Desc:A2A协作案例
"""
import os
import re
from datetime import datetime, timedelta
from typing import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage, HumanMessage
from langchain.tools import tool
from langchain.agents import create_agent  # LangChain 1.0 高层 Agent 构建 API

# ==================== 1. 大模型配置 =========================
llm = ChatOpenAI(
    model="qwen-plus",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0,
)


# ==================== 2. 业务工具 (@tool) ====================
# 每个工具就是一个领域能力的最小执行单元，子 Agent 通过 tool_calls 调用它们。
@tool("CtripBookFlight")
def ctrip_book_flight(departure: str, arrival: str, date: str) -> str:
    """预订机票。参数：departure 出发地、arrival 目的地、date 出行日期 (YYYY-MM-DD)。"""
    return (
        f"【携程机票预订成功】\n"
        f"出发地：{departure}\n目的地：{arrival}\n出行日期：{date}\n"
        f"航班号：CA1885（北京首都T3 → 上海浦东T2）\n"
        f"起飞时间：14:00\n降落时间：16:30\n"
        f"座位：经济舱34A\n电子客票号：999-1234567890"
    )


@tool("MeituanBookHotel")
def meituan_book_hotel(city: str, near_by: str, check_in: str, check_out: str) -> str:
    """预订酒店。参数：city 城市、near_by 地标、check_in 入住日期、check_out 离店日期。"""
    return (
        f"【美团酒店预订成功】\n"
        f"城市：{city}\n位置：{near_by}附近\n"
        f"入住日期：{check_in}\n离店日期：{check_out}\n"
        f"酒店名称：上海浦东机场铂尔曼大酒店\n"
        f"房型：豪华大床房（含双人自助早餐）\n"
        f"预订号：MT20260201001"
    )


@tool("DidiBookTaxi")
def didi_book_taxi(start: str, end: str, time: str) -> str:
    """预约打车。参数：start 起点、end 终点、time 用车时间 (YYYY-MM-DD HH:MM)。"""
    return (
        f"【滴滴打车预约成功】\n"
        f"起点：{start}\n终点：{end}\n用车时间：{time}\n"
        f"车型：滴滴快车（舒适型）\n"
        f"司机：王师傅 / 沪A12345 / 13800138000\n"
        f"预估费用：35元（券后实付30元）"
    )


# ==================== 3. run_tool_agent 工具执行器（通用逻辑）子 Agent 通用执行器 ====================
# create_agent() 返回的是 LangGraph 风格的 Agent，输入/输出都是 messages 列表：
#   输入: {"messages": [HumanMessage(...)]}
#   输出: {"messages": [..., AIMessage(...)]}
# 它内部已经实现了 "LLM 产 tool_calls → 执行工具 → 把 ToolMessage 喂回 LLM → 直至产出最终回复"的完整循环。
# 所以这里我们处理如下：
#   - 把用户任务包成 HumanMessage 发进去
#   - 从返回 messages 中找出最后一条 ToolMessage 的内容（即工具真实执行结果）
# 这样既保留了协调器与子 Agent 的解耦契约（输入字符串、输出工具结果字符串），
# 又用上了 create_agent 的标准化能力。

def run_tool_agent(agent, user_input: str, expected_tool: str) -> str:
    """
    执行一个由 create_agent 构建的子 Agent：
      1) 以 messages 形式驱动 Agent 完成一次工具调用循环
      2) 从消息历史中取出 expected_tool 的 ToolMessage 内容作为结果
    若 Agent 未调用预期工具，则抛出 RuntimeError，由协调器决定是否兜底。
    """
    # 官方create_agent 必须用 {"messages": [...]} 格式调用
    result = agent.invoke({"messages": [HumanMessage(content=user_input)]})
    # # 返回结果也是 messages 数组
    messages = result["messages"]
    print(f"*****>messages: {messages}")
    # 从后往前找最后一次 expected_tool 的执行结果（ToolMessage.name 与工具名一致）
    for msg in reversed(messages):
        if getattr(msg, "type", None) == "tool" and getattr(msg, "name", None) == expected_tool:
            return msg.content
    last: AIMessage = messages[-1]
    raise RuntimeError(f"子 Agent 未触发预期工具 {expected_tool}；模型回复：{last.content!r}")


# ==================== 4. 三个专属子 Agent ====================
# 每个子 Agent = create_agent(模型, 单一工具, 角色 system prompt)。
# 它们对外只暴露 invoke({"messages": [...]})，不感知彼此的存在。

def create_ctrip_agent():
    """携程机票 Agent：只会调用 CtripBookFlight。"""
    return create_agent(
        model=llm,
        tools=[ctrip_book_flight],
        system_prompt=(
            "你是携程机票预订助手。你必须且只能调用 CtripBookFlight 工具完成机票预订，"
            "从用户输入中抽取 departure / arrival / date 三个参数，日期格式 YYYY-MM-DD。"
        ),
    )


def create_meituan_agent():
    """美团酒店 Agent：只会调用 MeituanBookHotel。"""
    return create_agent(
        model=llm,
        tools=[meituan_book_hotel],
        system_prompt=(
            "你是美团酒店预订助手。你必须且只能调用 MeituanBookHotel 工具完成酒店预订，"
            "从用户输入中抽取 city / near_by / check_in / check_out 四个参数，日期格式 YYYY-MM-DD。"
        ),
    )


def create_didi_agent():
    """滴滴打车 Agent：只会调用 DidiBookTaxi。"""
    return create_agent(
        model=llm,
        tools=[didi_book_taxi],
        system_prompt=(
            "你是滴滴打车助手。你必须且只能调用 DidiBookTaxi 工具完成用车预约，"
            "从用户输入中抽取 start / end / time 三个参数，时间格式 YYYY-MM-DD HH:MM。"
        ),
    )


# ==================== 5. 行程计划数据结构 ====================
# 协调器用它在子 Agent 之间传递结构化上下文，避免 Agent 间互发自由文本。
class TripPlan(TypedDict):
    departure: str  # 出发城市
    arrival: str  # 到达城市
    date: str  # 出行日期 YYYY-MM-DD
    airport_terminal: str  # 机场航站楼（用作打车起点）
    near_by: str  # 酒店附近地标


# 第 1 步：解析用户需求,从自然语言提取：出发地、目的地、日期、机场、地标 → 结构化数据
def parse_user_request(text: str) -> TripPlan:
    """需求解析：从自然语言里抠出日期，其余字段回退到默认值。"""
    m = re.search(r"\d{4}-\d{2}-\d{2}", text)
    date = m.group(0) if m else "2026-02-01"
    return TripPlan(
        departure="北京",
        arrival="上海",
        date=date,
        airport_terminal="上海浦东机场T2",
        near_by="浦东机场",
    )


def add_minutes(date: str, hhmm: str, minutes: int) -> str:
    """把 'YYYY-MM-DD' + 'HH:MM' 偏移若干分钟，返回 'YYYY-MM-DD HH:MM'。"""
    dt = datetime.strptime(f"{date} {hhmm}", "%Y-%m-%d %H:%M") + timedelta(minutes=minutes)
    return dt.strftime("%Y-%m-%d %H:%M")


# ==================== 6. 总协调 Agent ====================
# 调度模式：Mediator —— 子 Agent 之间不直接对话，所有上下文经由协调器中转。
# 调度顺序由业务依赖决定：机票(决定到达时间) → 酒店(决定打车终点) → 打车。

def create_travel_coordinator(ctrip_chain, meituan_chain, didi_chain):
    # 内部定义真正的执行函数
    def coordinate(payload: dict) -> str:
        # 1. 解析用户需求 → 结构化行程计划
        plan = parse_user_request(payload["input"])
        print(f"🧭 解析需求 → {plan}\n")

        # ---- ① 机票 第 2 步：派发任务给机票 Agent---------------------------------------------------
        print("① 派发任务给【携程机票 Agent】")
        flight_task = (
            f"请预订{plan['date']}从{plan['departure']}到{plan['arrival']}的机票。"
        )
        try:
            # 第 2 步：派发任务给机票 Agent
            # 子 Agent 生成工具调用参数 - 执行机票预订 -提取降落时间（给打车用）
            flight_result = run_tool_agent(ctrip_chain, flight_task, "CtripBookFlight")
        except Exception as e:
            print(f"   ⚠️ 子 Agent 调用失败，启用兜底直调工具：{e}")
            flight_result = ctrip_book_flight.invoke({
                "departure": plan["departure"],
                "arrival": plan["arrival"],
                "date": plan["date"],
            })
        print(f"   ✅ 携程返回：\n{flight_result}\n" + "-" * 70)

        # 从携程结果中抽取降落时间，作为打车时间的依据（A2A 上下文传递的关键一步）
        landing_match = re.search(r"降落时间：(\d{2}:\d{2})", flight_result)
        landing_hhmm = landing_match.group(1) if landing_match else "16:30"
        pickup_time = add_minutes(plan["date"], landing_hhmm, 10)

        # ---- ② 酒店 第 3 步：派发任务给酒店 Agent---------------------------------------------------
        print("② 派发任务给【美团酒店 Agent】")
        check_out = (datetime.strptime(plan["date"], "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        hotel_task = (
            f"请在{plan['arrival']}{plan['near_by']}附近预订酒店，"
            f"入住 {plan['date']}，离店 {check_out}。"
        )
        try:
            # 第 3 步：派发任务给酒店 Agent
            # 预订酒店,提取酒店名称（给打车当终点）
            hotel_result = run_tool_agent(meituan_chain, hotel_task, "MeituanBookHotel")
        except Exception as e:
            print(f"   ⚠️ 子 Agent 调用失败，启用兜底直调工具：{e}")
            hotel_result = meituan_book_hotel.invoke({
                "city": plan["arrival"],
                "near_by": plan["near_by"],
                "check_in": plan["date"],
                "check_out": check_out,
            })
        print(f"   ✅ 美团返回：\n{hotel_result}\n" + "-" * 70)

        # 从酒店结果中抽取酒店名称，作为打车终点
        hotel_match = re.search(r"酒店名称：(.+)", hotel_result)
        hotel_name = hotel_match.group(1).strip() if hotel_match else "上海浦东机场铂尔曼大酒店"

        # ---- ③ 打车（依赖 ① 的降落时间 + ② 的酒店名）第 4 步：派发任务给打车 Agent---------------------
        print("③ 派发任务给【滴滴打车 Agent】（依赖前两步结果）")
        taxi_task = (
            f"请预约一辆从 {plan['airport_terminal']} 到 {hotel_name} 的车，"
            f"用车时间 {pickup_time}。"
        )
        try:
            # 第 4 步：派发任务给打车 Agent
            # 起点：机场航站楼-终点：酒店名称-时间：降落 + 10 分钟
            taxi_result = run_tool_agent(didi_chain, taxi_task, "DidiBookTaxi")
        except Exception as e:
            print(f"   ⚠️ 子 Agent 调用失败，启用兜底直调工具：{e}")
            taxi_result = didi_book_taxi.invoke({
                "start": plan["airport_terminal"],
                "end": hotel_name,
                "time": pickup_time,
            })
        print(f"   ✅ 滴滴返回：\n{taxi_result}\n" + "-" * 70)

        # ---- 汇总报告 第 5 步：汇总报告返回-------------------------------------------------
        return (
                "📋 A2A 协作最终报告\n"
                + "=" * 70 + "\n"
                + f"协作链路：用户 → 协调器 → 携程 → 协调器 → 美团 → 协调器 → 滴滴\n"
                + f"上下文接力：航班降落 {landing_hhmm} +10min ⇒ 打车时间 {pickup_time}；"
                  f"酒店名 ⇒ 打车终点\n"
                + "=" * 70 + "\n"
                + f"\n【1. 机票】\n{flight_result}\n"
                + f"\n【2. 酒店】\n{hotel_result}\n"
                + f"\n【3. 打车】\n{taxi_result}\n"
                + "=" * 70
        )

    # RunnableLambda = 把一个普通 Python 函数，包装成 LangChain 可执行的标准组件
    return RunnableLambda(coordinate)


# ==================== 7. 入口 ====================
if __name__ == "__main__":
    try:
        print("🔧 初始化3个子Agent...")
        ctrip_chain = create_ctrip_agent()
        meituan_chain = create_meituan_agent()
        didi_chain = create_didi_agent()

        print("🔧 初始化总协调者Agent...\n" + "=" * 70)
        coordinator = create_travel_coordinator(ctrip_chain, meituan_chain, didi_chain)

        print("🚀 开始 A2A 协作\n")
        report = coordinator.invoke({"input": "安排2026-02-01北京飞上海的完整行程"})
        print("\n" + report)

    except Exception as e:
        print(f"❌ 全局异常：{type(e).__name__} - {e}")
        print("排查：\n"
              "1) 环境变量 aliQwen-api 是否设置  "
              "2) 网络能否访问 dashscope.aliyuncs.com  "
              "3) langchain / langchain-openai 版本是否匹配 LangChain 1.0")

"""
设计要点回顾
─────────────
1. 子 Agent 单一职责：每个 Agent 只绑定一个工具，Prompt 强约束它必须调用该工具。
2. 执行tool-calling：run_tool_agent 直接消费 AIMessage.tool_calls
3. Mediator调度：子 Agent 之间不互相 import / 不互发消息，全部由协调器中转，
   降低耦合，方便后续替换为 LangGraph 的 StateGraph。
4. 上下文接力：协调器用 TripPlan + 正则从上一步结果中抽取关键字段，
   作为下一步的输入参数，体现 A2A 真实价值（不是三个独立任务的拼接）。
5. 失败兜底：每一步保留"直调原始工具"的退路，保证演示稳定，同时把异常打印出来，便于调试。
    代码里有非常健壮的容错设计：
    子 Agent 调用失败,模型不返回 tool_calls,参数抽取错误→ 系统不会崩，直接兜底执行
    try:
        子Agent执行
    except:
        直接调用工具（硬编码参数）

完整运行流程总结
业务依赖严格顺序：机票 → 酒店 → 打车（必须按业务逻辑串行执行）
1 用户输入
    安排2026-02-01北京飞上海的完整行程

2 协调器解析 → 生成结构化 TripPlan

3 调用机票 Agent（create_agent）
    输入：{"messages": ["订机票"]}
    内部：LLM 思考 → 调用工具 → 返回结果
    输出：ToolMessage（机票成功）

4 协调器提取：降落时间 携程的"降落时间 + 10 分钟" ───────────▶ ③ 滴滴的 time

5 调用酒店 Agent
    输入：城市、位置、日期
    输出：酒店名称

6 协调器提取：酒店名称

7 调用打车 Agent
    起点：机场
    终点：酒店
    时间：降落 + 10 分钟

8 汇总报告

"""