from langchain_core.prompts import ChatPromptTemplate
from app.models.llms.groq_llm import get_groq_llm

llm = get_groq_llm()

judge_prompt = ChatPromptTemplate.from_template("""
Eres un evaluador experto de contenido generado por IA.

Evalúa la siguiente respuesta según estos criterios:
- Claridad
- Corrección factual
- Utilidad
- Adecuación al contexto
- Riesgo de alucinación

Devuelve SOLO este formato:

SCORE: <número de 0 a 10>
FEEDBACK: <breve explicación>

Pregunta original:
{question}

Respuesta generada:
{answer}
""")

def evaluate_answer(question: str, answer: str) -> dict:
    response = llm.invoke(
        judge_prompt.format(
            question=question,
            answer=answer
        )
    )

    text = response.content

    score = 0
    feedback = ""

    for line in text.splitlines():
        if line.startswith("SCORE"):
            score = int(line.split(":")[1].strip())
        if line.startswith("FEEDBACK"):
            feedback = line.split(":")[1].strip()

    return {
        "score": score,
        "feedback": feedback
    }
