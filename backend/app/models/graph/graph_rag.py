from langchain_core.prompts import ChatPromptTemplate
from app.models.llms.groq_llm import get_groq_llm
from app.models.graph.knowledge_graph import KnowledgeGraph
import json

llm = get_groq_llm()

extract_prompt = ChatPromptTemplate.from_template("""
Extrae entidades y relaciones del siguiente texto científico.

Devuelve SOLO JSON con este formato:
{
  "entities": [{"name": "...", "type": "..."}],
  "relations": [{"source": "...", "target": "...", "relation": "..."}]
}

Texto:
{input}
""")

def build_graph_from_text(text: str) -> KnowledgeGraph:
    response = llm.invoke(extract_prompt.format(input=text))
    data = json.loads(response.content)

    kg = KnowledgeGraph()

    for ent in data["entities"]:
        kg.add_entity(ent["name"], ent["type"])

    for rel in data["relations"]:
        kg.add_relation(rel["source"], rel["target"], rel["relation"])

    return kg

query_prompt = ChatPromptTemplate.from_template("""
Usa el siguiente grafo de conocimiento para responder la pregunta.

Grafo:
{graph}

Pregunta:
{question}
""")

def query_graph(kg: KnowledgeGraph, question: str) -> str:
    graph_text = kg.to_text()
    return llm.invoke(
        query_prompt.format(graph=graph_text, question=question)
    ).content
