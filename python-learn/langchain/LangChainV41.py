"""
  @Author:lining-lo
  @Time:2026/7/4
  @Desc:文本加载器
"""
# pip install langchain_community unstructured[docx]
# pip install -U unstructured
# pip install python-docx
# pip install regex==2026.1.14
# pip install jq
# pip install langchain_community unstructured[md]

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_community.document_loaders.csv_loader import CSVLoader


def csvloader_demo():
    # 加载所有列
    docs = CSVLoader(
        file_path="assets/sample.csv",  # 文件路径
    ).load()  # 返回List[Document]

    print(docs)

    # 加载部分列
    docs = CSVLoader(
        file_path="assets/sample.csv",  # 文件路径
        metadata_columns=["title", "author"],  # 将指定列作为元数据
        content_columns=["content"],  # 将指定列作为内容
    ).load()  # 返回List[Document]

    print(docs)


def documentloader_demo():
    docs = UnstructuredWordDocumentLoader(
        # 文件路径
        file_path="assets/alibaba-more.docx",
        # 加载模式:
        #   single 返回单个Document对象
        #   elements 按标题等元素切分文档
        mode="single",
    ).load()

    print(docs)


def jsonloader_demo():
    # 提取所有字段
    docs = JSONLoader(
        file_path="assets/sample.json",  # 文件路径
        jq_schema=".",  # 提取所有字段
        text_content=False,  # 提取内容是否为字符串格式
    ).load()

    print(docs)


def markdownloader_demo():
    docs = UnstructuredMarkdownLoader(
        # 文件路径
        file_path="assets/sample.md",
        # 加载模式:
        #   single 返回单个Document对象
        #   elements 按标题等元素切分文档
        mode="elements",
    ).load()

    print(docs)


def pdfloader_demo():
    docs = PyPDFLoader(
        # 文件路径，支持本地文件和在线文件链接，如"https://arxiv.org/pdf/alg-geom/9202012"
        file_path="assets/sample.pdf",
        # 提取模式:
        #   plain 提取文本
        #   layout 按布局提取
        extraction_mode="plain",
    ).load()

    print(docs)


def textloader_demo():
    # 返回List[Document]
    file_path = "assets/sample.txt"  # 文件路径
    encoding = "utf-8"  # 文件编码方式

    docs = TextLoader(file_path, encoding).load()

    print(docs)


if __name__ == '__main__':
    # csvloader_demo()
    # documentloader_demo()
    # jsonloader_demo()
    # markdownloader_demo()
    # pdfloader_demo()
    textloader_demo()