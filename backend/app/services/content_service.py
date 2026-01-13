from app.models.agents.router_agent import route
from app.models.agents.memory import ConversationMemory
from app.services.rag_service import rag_answer, graph_rag_answer
from app.models.agents.marketing_agent import marketing_agent
from app.models.agents.judge_agent import evaluate_answer

memory = ConversationMemory()

def generate_content(question: str) -> dict:
    memory.add("user", question)

    strategy = route(question)

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

    memory.add("assistant", answer)

    return {
        "answer": answer,
        "evaluation": evaluation,
        "strategy_used": strategy
    }

