from app.models.rag.arxiv_loader import load_arxiv_documents
from app.models.rag.text_splitter import split_documents
from app.models.rag.vector_store import create_vectorstore
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from app.models.graph.graph_rag import build_graph_from_text, query_graph

load_dotenv()


class RAGService:

    def __init__(self):
        self.llm = ChatGroq(
            model="llama3-8b-8192",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_scientific_content(self, query: str) -> str:
        # 1. Cargar documentos
        documents = load_arxiv_documents(query)

        # 2. Split
        chunks = split_documents(documents)

        # 3. Vector store
        vectorstore = create_vectorstore(chunks)

        # 4. Retriever
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # 5. Recuperar contexto
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        # 6. Prompt RAG
        prompt = f"""
        Usa el siguiente contexto científico para responder de forma divulgativa:

        {context}

        Pregunta:
        {query}
        """

        response = self.llm.invoke(prompt)
        return response.content


# Funciones helper para compatibilidad
def rag_answer(question: str) -> str:
    """Genera respuesta usando RAG científico"""
    service = RAGService()
    return service.generate_scientific_content(question)


def graph_rag_answer(text: str, question: str) -> str:
    kg = build_graph_from_text(text)
    return query_graph(kg, question)