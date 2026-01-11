from langchain_core.prompts import ChatPromptTemplate
from app.models.agents.base_agent import BaseAgent
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

marketing_prompt = ChatPromptTemplate.from_template("""
Eres un experto creador de contenido digital.

Tema: {tema}
Plataforma: {plataforma}
Audiencia: {audiencia}
Tono: {tono}

Genera contenido listo para publicar.
""")

marketing_chain = marketing_prompt | llm
marketing_agent = BaseAgent(marketing_chain)
