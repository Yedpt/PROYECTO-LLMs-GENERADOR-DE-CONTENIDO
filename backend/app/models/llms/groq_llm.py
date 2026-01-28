import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Cargar variables de entorno desde la raíz del proyecto
load_dotenv()

def get_groq_llm():
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY no está configurada en el archivo .env")
    
    return ChatGroq(
        model="llama-3.1-8b-instant",  # Modelo actualizado
        temperature=0.3,
        api_key=api_key
    )
