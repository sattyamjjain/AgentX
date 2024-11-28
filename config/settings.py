import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
WHISPER_API_KEY = os.getenv("WHISPER_API_KEY", "")

DATA_PATH = BASE_DIR / "data"
DOCUMENTS_PATH = DATA_PATH / "documents"
AUDIO_PATH = DATA_PATH / "audio"
LOG_PATH = BASE_DIR / "logs"

AGENT_NAME = "AgentX"
TEMPERATURE = 0.7
MAX_TOKENS = 1024

DEBUG = os.getenv("DEBUG", "True").lower() == "true"
