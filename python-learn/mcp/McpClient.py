"""
  @Author:lining-lo
  @Time:2026/7/5
  @Desc:MCP客户端
"""
# pip install uv

import asyncio
import json
import os
from typing import Any, Dict
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from loguru import logger
from langchain.agents import create_agent


# 加载mcp.json配置文件，读取所有MCP服务配置
def load_servers(file_path: str = "mcp.json") -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        # 只返回配置里的mcpServers节点（weather、fetch两个服务）
        return data.get("mcpServers", {})


# 异步主对话循环函数
async def run_chat_loop() -> None:
    # 1. 读取本地MCP服务配置
    servers_cfg = load_servers()
    # 2. 创建多服务MCP客户端，自动连接所有SSE+STDIO服务
    mcp_client = MultiServerMCPClient(servers_cfg)
    # 3. 异步获取所有MCP暴露的工具（天气查询、网页抓取）
    tools = await mcp_client.get_tools()
    # 打印成功加载的工具名称与数量
    logger.info(f"已加载 {len(tools)} 个 MCP 工具： {[t.name for t in tools]}")

    # 初始化DeepSeek大模型
    llm = init_chat_model(
        model="deepseek-v4-pro",
        api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从环境变量读取密钥
        base_url="https://api.deepseek.com",
        # 关闭模型内置思考输出，只返回最终答案
        extra_body={"thinking": {"type": "disabled"}}
    )

    # 构建智能Agent：绑定大模型 + 全部MCP工具 + 系统提示词
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "你是AI智能运维助手，必须使用工具回答问题。"
            "可以调用天气、网页抓取工具，准确回答用户问题。"
        )
    )

    logger.info("\n🤖AI智能运维助手已启动，输入 'quit' 退出")
    # 循环对话交互
    while True:
        user_input = input("\n你: ").strip()

        # 输入quit结束会话
        if user_input.lower() == "quit":
            break

        try:
            # 异步调用Agent，自动判断是否需要调用MCP工具
            result = await agent.ainvoke({"messages": [("user", user_input)]})
            # 取出最后一条AI回复内容打印
            print(f"\nAI: {result['messages'][-1].content}")
        except Exception as exc:
            # 捕获运行异常并打印日志
            logger.error(f"\n异常出错: {exc}")

    logger.info("======》会话已结束，Bye!")


if __name__ == "__main__":
    print("---------启动中---------\n")
    # 提供两个测试提问示例
    print("测试案例:"
          "① 北京天气如何：正常返回天气数据\n"
          "② MCP文档总结：返回完整文档摘要（警告为依赖提示，不影响）")

    # 启动异步对话主函数
    asyncio.run(run_chat_loop())
