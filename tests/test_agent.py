from core.agent import AgentX


def test_agent_initialization():
    agent = AgentX()
    assert agent.llm is not None
    assert agent.vector_store is not None
