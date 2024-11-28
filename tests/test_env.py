import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import OPENAI_API_KEY, DEBUG, AGENT_NAME

print("Agent Name:", AGENT_NAME)
print("OpenAI API Key:", OPENAI_API_KEY)
print("Debug Mode:", DEBUG)
