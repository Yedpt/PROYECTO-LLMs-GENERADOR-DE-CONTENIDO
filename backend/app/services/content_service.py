import os
from dotenv import load_dotenv
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
