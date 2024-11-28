from langchain.memory import ConversationBufferMemory
from utils.logger import get_logger

logger = get_logger("MemoryHandler")


class MemoryHandler:
    def __init__(self):
        self.memory = ConversationBufferMemory(return_messages=True)
        logger.info("MemoryHandler initialized.")

    def add_to_memory(self, user_input, agent_response):
        logger.debug(f"Adding to memory: input={user_input}, response={agent_response}")
        self.memory.save_context({"input": user_input}, {"output": agent_response})

    def get_memory(self):
        logger.debug("Retrieving memory history.")
        return self.memory.chat_memory
