import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from config.settings import OPENAI_API_KEY, TEMPERATURE
from config.constants import VOSK_MODEL_DIR
from core.memory import MemoryHandler
from core.document_handler import DocumentHandler
from core.voice_processor import VoiceProcessor
from utils.logger import get_logger

logger = get_logger("AgentX")


class AgentX:
    def __init__(self):
        logger.info("Initializing AgentX...")
        try:
            self.llm = ChatOpenAI(
                temperature=TEMPERATURE, openai_api_key=OPENAI_API_KEY
            )
            document_handler = DocumentHandler()
            documents = document_handler.load_documents()
            embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
            self.vector_store = FAISS.from_documents(documents, embedding=embeddings)
            retriever = self.vector_store.as_retriever()

            self.memory_handler = MemoryHandler()

            prompt_template = ChatPromptTemplate.from_template(
                "You are AgentX, a helpful assistant. Based on the following context, answer the question: {context}\n\nQuestion: {input}"
            )
            combine_docs_chain = create_stuff_documents_chain(
                llm=self.llm, prompt=prompt_template
            )

            self.conversation_chain = create_retrieval_chain(
                retriever=retriever, combine_docs_chain=combine_docs_chain
            )

            self.voice_processor = VoiceProcessor(model_path=VOSK_MODEL_DIR)
            logger.info("AgentX initialized successfully.")
        except Exception as e:
            logger.error(f"Error during AgentX initialization: {e}")
            raise

    def run(self):
        logger.info("AgentX is ready to assist you! Say 'exit' to quit.")
        while True:
            try:
                user_input = self.voice_processor.record_audio()
                if user_input.lower() == "exit":
                    logger.info("Exit command received. Terminating AgentX.")
                    print("Goodbye!")
                    break

                chat_history = self.memory_handler.get_memory()
                response = self.conversation_chain.invoke(
                    {"input": user_input, "chat_history": chat_history}
                )

                self.memory_handler.add_to_memory(user_input, response["answer"])

                print(f"AgentX: {response['answer']}")
                self.voice_processor.text_to_speech(response["answer"])
                logger.info(f"Processed input: {user_input}")
            except Exception as e:
                logger.error(f"Error during runtime: {e}")
