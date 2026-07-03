"""
  @Author:lining-lo
  @Time:2026/7/2
  @Desc:python连接RedisStack
"""
# pip install redis==5.3.1

# 极简 redis 导入测试脚本
try:
    # 导入 redis 包
    import redis

    print("✅ redis 包导入成功！")
    print(f"✅ redis 包版本：{redis.__version__}")
except ModuleNotFoundError:
    print("❌ 未找到 redis 包，请先安装！")
except Exception as e:
    print(f"❌ redis 包导入异常：{e}")
