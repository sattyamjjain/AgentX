import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.logger import get_logger

logger = get_logger("DocumentHandler")


class DocumentHandler:
    def __init__(self, directory="data/documents"):
        self.directory = directory
        logger.info(f"DocumentHandler initialized with directory: {self.directory}")

    def load_documents(self):
        logger.info("Loading documents...")
        documents = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if filename.endswith(".txt") and os.path.isfile(file_path):
                logger.info(f"Loading file: {filename}")
                try:
                    loader = TextLoader(file_path)
                    documents.extend(loader.load())
                except Exception as e:
                    logger.error(f"Error loading file {filename}: {e}")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        split_docs = text_splitter.split_documents(documents)
        logger.info(f"Loaded {len(split_docs)} document chunks.")
        return split_docs
