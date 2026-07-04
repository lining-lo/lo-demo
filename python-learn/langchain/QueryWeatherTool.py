"""
  @Author:lining-lo
  @Time:2026/7/4
  @Desc:定义OpenWeatherAPI查询天气的工具
"""
import random

from langchain_core.tools import tool
import json
import os
import httpx
from dotenv import load_dotenv  # 导入读取.env工具

# 加载同目录下 .env 文件中的所有环境变量
load_dotenv()

@tool
def get_weather(loc):
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
        "q": loc,
        "appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key
        # "appid": "fc19f7b552b4c1ae467e36fe69556668",  # 硬编码写死 API Key
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }

    # Step 3. 发送 GET 请求获取天气数据 @GetMapping
    response = httpx.get(url, params=params, timeout=30)

    # Step 4. 解析响应内容为 JSON 并序列化为字符串返回
    data = response.json()
    # print(json.dumps(data))
    return json.dumps(data)


# 测试
cityList = ["beijing", "shanghai", "chengdu", "guangzhou"]
targetCity = random.choice(cityList)
result = get_weather.invoke(targetCity)
print(result)

# 网络报错，多调试几次或者等。。。。。。
# httpx.ConnectTimeout: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。


