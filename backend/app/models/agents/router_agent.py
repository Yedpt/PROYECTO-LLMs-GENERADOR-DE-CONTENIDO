from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

router_prompt = ChatPromptTemplate.from_template("""
Clasifica la siguiente petición en una categoría:

- marketing
- science

Petición: {input}

Responde SOLO con una palabra.
""")

router_chain = router_prompt | llm

def route_request(text: str) -> Literal["marketing", "science"]:
    return router_chain.invoke({"input": text}).strip().lower()
