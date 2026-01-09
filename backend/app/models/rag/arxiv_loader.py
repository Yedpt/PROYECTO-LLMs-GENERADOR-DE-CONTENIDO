from langchain_community.document_loaders import ArxivLoader
from langchain_core.documents import Document
from typing import List


def load_arxiv_documents(query: str, max_docs: int = 5) -> List[Document]:
    loader = ArxivLoader(query=query, max_docs=max_docs)
    return loader.load()
