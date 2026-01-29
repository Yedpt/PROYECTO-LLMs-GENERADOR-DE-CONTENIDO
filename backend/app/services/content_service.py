from app.models.agents.router_agent import route
from app.models.agents.memory import ConversationMemory
from app.services.rag_service import rag_answer, graph_rag_answer
from app.models.agents.marketing_agent import marketing_agent
from app.models.agents.judge_agent import evaluate_answer
from app.config.quality_config import (
    MIN_SCORE,
    MAX_RETRIES,
    FALLBACK_MESSAGE
)
from app.utils.logger import logger
from app.models.llms.groq_llm import get_groq_llm
from app.services.image_service import generate_image
import time


memory = ConversationMemory()


class ContentService:
    """Servicio para generar contenido usando LLM"""

    def __init__(self):
        self.llm = get_groq_llm()

    def generar_contenido(
        self,
        tema: str,
        plataforma: str,
        audiencia: str,
        tono: str
    ) -> dict:
        """Genera contenido + imagen"""

        prompt = f"""
        Eres un experto creador de contenido digital.

        Tema: {tema}
        Plataforma: {plataforma}
        Audiencia: {audiencia}
        Tono: {tono}

        Genera un texto listo para publicar, adaptado a la plataforma indicada.
        """

        response = self.llm.invoke(prompt)
        content = response.content

        image_prompt = (
            f"High quality illustration for a {plataforma} post about {tema}, "
            f"targeted at {audiencia}, modern, clean, professional, digital art"
        )

        image_url = generate_image(image_prompt)

        return {
            "content": content,
            "image_url": image_url
        }


# ⚠️ TU SISTEMA AVANZADO NO SE TOCA
def generate_content(question: str) -> dict:
    start_time = time.time()
    logger.info(f"New request received: {question}")

    memory.add("user", question)

    retries = 0

    while retries <= MAX_RETRIES:
        strategy = route(question)
        logger.info(f"Strategy selected: {strategy}")

        if strategy == "graph_rag":
            answer = graph_rag_answer(
                text=question,
                question=question
            )
        elif strategy == "multiagent":
            answer = marketing_agent(question)
        else:
            answer = rag_answer(question)

        evaluation = evaluate_answer(question, answer)
        logger.info(
            f"Evaluation score: {evaluation['score']} | Retry: {retries}"
        )

        if evaluation["score"] >= MIN_SCORE:
            elapsed = round(time.time() - start_time, 2)
            logger.info(f"Request completed in {elapsed}s")

            memory.add("assistant", answer)

            return {
                "answer": answer,
                "evaluation": evaluation,
                "strategy_used": strategy,
                "retries": retries,
                "time_seconds": elapsed
            }

        retries += 1

    logger.warning("Fallback response returned")

    return {
        "answer": FALLBACK_MESSAGE,
        "evaluation": {
            "score": 0,
            "feedback": "Respuesta rechazada por baja calidad."
        },
        "strategy_used": None,
        "retries": retries
    }
