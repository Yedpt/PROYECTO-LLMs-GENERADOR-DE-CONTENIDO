from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        temperature=0.3
    )
