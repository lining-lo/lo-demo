"""
  @Author:lining-lo
  @Time:2026/7/5
  @Desc:MCP服务端
"""
import json
import os
import httpx
from mcp.server.fastmcp import FastMCP
from loguru import logger
from dotenv import load_dotenv

#  该案例跑在python3.12.7及以下
# 一个MCPServer对外暴露多个，一系列TOOLCalling工具类的集合

# 加载同目录下 .env 文件中的所有环境变量
load_dotenv()

# 创建FastMCP实例，用于启动天气服务器SSE服务
mcp = FastMCP("WeatherServerSSE", host="0.0.0.0", port=8000)

@mcp.tool()
def get_weather(city: str) -> str:
    """
        查询即时天气函数

        :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称。
                    注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，
                    则 loc 参数需要输入 'Beijing'/'shanghai'。
        :return: OpenWeather API 查询即时天气的结果。具体 URL 请求地址为：
                 https://home.openweathermap.org/users/sign_in。
                 返回结果对象类型为解析之后的 JSON 格式对象，并用字符串形式进行表示，
                 其中包含了全部重要的天气信息。
        """
    # Step 1. 构建请求 URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Step 2. 设置查询参数，包括城市名、API Key、单位和语言
    # 程序没错，但是实际偶尔会有调用不成功的情况
    params = {
        "q": city,
         "appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }

    # Step 3. 发送 GET 请求获取天气数据 @GetMapping
    response = httpx.get(url, params=params, timeout=30)

    # Step 4. 解析响应内容为 JSON 并序列化为字符串返回
    data = response.json()
    logger.info(f"查询 {city} 天气结果：{data}")
    return json.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
    logger.info("启动 MCP SSE 天气服务器，监听 http://0.0.0.0:8000/sse")
    # 运行MCP客户端，使用Server-Sent Events(SSE)作为传输协议
    mcp.run(transport="sse")
    #mcp.run(transport="stdio")

'''
核心重点：202 Accepted 状态码的意义（结合 MCP SSE 场景）
HTTP 202 状态码和常见的200 OK有本质区别，适配 MCP SSE 的流式处理特性：
200 OK：请求已处理完成，服务端立即返回最终结果（适合一次性请求 - 响应的场景，比如普通接口查询）；
202 Accepted：请求已接收并受理，服务端会在后台处理（比如调用天气工具、执行 MCP 指令），
处理完成后通过 SSE 流将结果推送给客户端（适合耗时 / 流式处理的场景，这正是 MCP SSE 服务的设计逻辑）。
'''