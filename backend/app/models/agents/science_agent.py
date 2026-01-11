from langchain_core.prompts import ChatPromptTemplate
from app.models.agents.base_agent import BaseAgent
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

science_prompt = ChatPromptTemplate.from_template("""
Eres un divulgador científico experto.

Tema: {tema}

Explica el concepto de forma rigurosa pero accesible
para el público general.
""")

science_chain = science_prompt | llm
science_agent = BaseAgent(science_chain)
