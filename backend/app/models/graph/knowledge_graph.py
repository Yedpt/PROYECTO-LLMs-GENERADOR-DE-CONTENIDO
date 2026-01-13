import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_entity(self, name: str, entity_type: str):
        self.graph.add_node(name, type=entity_type)

    def add_relation(self, source: str, target: str, relation: str):
        self.graph.add_edge(source, target, relation=relation)

    def get_subgraph(self, nodes: list[str]):
        return self.graph.subgraph(nodes)

    def to_text(self) -> str:
        lines = []
        for u, v, data in self.graph.edges(data=True):
            lines.append(f"{u} --[{data['relation']}]--> {v}")
        return "\n".join(lines)
