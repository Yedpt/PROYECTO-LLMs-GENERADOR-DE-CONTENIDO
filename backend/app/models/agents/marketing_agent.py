from langchain_core.prompts import ChatPromptTemplate
from app.models.agents.base_agent import BaseAgent
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

marketing_prompt = ChatPromptTemplate.from_template("""
Eres un experto creador de contenido digital.

Genera contenido creativo y relevante para la siguiente solicitud:

{question}
""")

marketing_chain = marketing_prompt | llm


def marketing_agent(question: str) -> str:
    """Genera contenido de marketing usando el agente"""
    response = marketing_chain.invoke({"question": question})
    return response.content
