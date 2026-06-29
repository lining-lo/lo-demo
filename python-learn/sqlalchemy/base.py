"""
  @Author:lining-lo
  @Time:2026/6/29
  @Desc:Base基类
"""
from sqlalchemy.ext.declarative import declarative_base

# 生成基类,所有模型需继承该类
Base = declarative_base()
