from langchain_core.output_parsers import StrOutputParser
from app.models.llms.groq_llm import get_groq_llm

class BaseAgent:
    def __init__(self, chain):
        self.chain = chain

    def invoke(self, input_data: dict) -> str:
        return self.chain.invoke(input_data)
