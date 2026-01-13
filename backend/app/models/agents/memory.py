class ConversationMemory:
    def __init__(self, max_messages: int = 5):
        self.max_messages = max_messages
        self.messages = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_context(self) -> str:
        return "\n".join(
            f"{m['role']}: {m['content']}" for m in self.messages
        )
