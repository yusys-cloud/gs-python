"""
@Time    : 2023/12/30 23:04
@Author  : yangzq80@gmail.com
@File    : load_web.py
"""

from langchain.document_loaders import TextLoader,WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from loguru import logger

loader = WebBaseLoader('https://docs.spring.io/spring-security/site/docs/5.3.0.RELEASE/reference/html5/#authz-hierarchical-roles')

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

docs=loader.load_and_split(text_splitter)

logger.info(len(docs))

# logger.info(docs[10].page_content())

