from langchain_core.messages import HumanMessage

from core.memory import MemoryHandler


def test_memory_handler():
    memory = MemoryHandler()
    memory.add_to_memory("What is Python?", "Python is a programming language.")
    history = memory.get_memory()

    assert len(history.messages) > 0
    assert isinstance(history.messages[0], HumanMessage)
    assert history.messages[0].content == "What is Python?"
