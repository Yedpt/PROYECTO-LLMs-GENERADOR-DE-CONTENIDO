import os
from dotenv import load_dotenv
from app.models.agents.router_agent import route_request
from app.models.agents.marketing_agent import marketing_agent
from app.models.agents.science_agent import science_agent
from langchain_groq import ChatGroq

load_dotenv()

class ContentService:

    def __init__(self):
        self.llm = ChatGroq(
            model="llama3-8b-8192",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generar_contenido(
        self,
        tema: str,
        plataforma: str,
        audiencia: str,
        tono: str
    ) -> str:

        prompt = f"""
        Eres un experto creador de contenido digital.

        Tema: {tema}
        Plataforma: {plataforma}
        Audiencia: {audiencia}
        Tono: {tono}

        Genera un texto listo para publicar, adaptado a la plataforma indicada.
        """

        response = self.llm.invoke(prompt)
        return response.content


def multiagent_generate(input_text: str, payload: dict) -> str:
    route = route_request(input_text)

    if route == "science":
        return science_agent.invoke(payload)

    return marketing_agent.invoke(payload)