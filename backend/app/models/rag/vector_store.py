from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List
from app.models.rag.embeddings import get_embeddings


def create_vectorstore(chunks: List[Document]) -> Chroma:
    embeddings = get_embeddings()

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./data/vectorstore"
    )
