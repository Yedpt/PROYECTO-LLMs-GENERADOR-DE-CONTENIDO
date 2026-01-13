from langchain_core.prompts import ChatPromptTemplate
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

router_prompt = ChatPromptTemplate.from_template("""
Eres un sistema experto que decide qué estrategia usar.

Opciones:
- rag
- graph_rag
- multiagent

Decide SOLO una opción.

Pregunta:
{question}
""")

def route(question: str) -> str:
    response = llm.invoke(router_prompt.format(question=question))
    decision = response.content.lower()

    if "graph" in decision:
        return "graph_rag"
    if "multi" in decision:
        return "multiagent"
    return "rag"
