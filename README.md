
# AgentX

AgentX is an advanced AI-powered assistant that integrates voice processing, document retrieval, conversational memory, and generative AI capabilities. This agent is designed to handle a wide range of tasks, from answering queries to processing voice commands.

---

## Features

1. **Voice Recognition**
   - Converts speech to text using Vosk models.
   - Processes voice commands and generates audio responses via Google Text-to-Speech (gTTS).

2. **Document Retrieval**
   - Utilizes FAISS for efficient document embedding and retrieval.
   - Supports multiple document types for context-aware responses.

3. **Generative AI**
   - Powered by OpenAI GPT models for conversational capabilities.
   - Generates meaningful responses based on retrieved documents and context.

4. **Conversational Memory**
   - Maintains context across interactions using LangChain's `ConversationBufferMemory`.

5. **Integration Ready**
   - Modular design to integrate additional tools like Whisper API, advanced LangChain tools, or scheduling tasks.

---

## Tech Stack

| **Tool**               | **Purpose**                                    |
|-------------------------|-----------------------------------------------|
| **LangChain**          | Conversational chains and memory handling     |
| **OpenAI GPT**         | Language generation and query answering       |
| **Vosk**               | Speech-to-text offline transcription          |
| **gTTS**               | Text-to-speech conversion                     |
| **FAISS**              | Document embedding and vector retrieval       |
| **playsound**          | Audio playback                                |
| **dotenv**             | Environment variable management               |
| **pytest**             | Unit testing framework                        |
| **Logging**            | Structured logging for debugging              |

---

## Project Structure

```
.
├── config
│   ├── constants.py        # Reusable constants
│   ├── settings.py         # Application settings and environment variables
├── core
│   ├── agent.py            # Main agent logic
│   ├── document_handler.py # Document loading and splitting
│   ├── memory.py           # Conversational memory handler
│   ├── voice_processor.py  # Voice processing logic
├── data
│   ├── documents           # Sample documents for testing
│   ├── audio               # Audio files (input/output)
├── model
│   └── vosk-model-small-en-us-0.15  # Speech recognition model
├── scripts
│   ├── run_agent.sh        # Script to run the agent
│   ├── setup_env.sh        # Script to set up the environment
├── tests
│   ├── test_agent.py       # Tests for agent.py
│   ├── test_memory.py      # Tests for memory handler
│   ├── test_voice_processor.py  # Tests for voice processing
├── Dockerfile              # Docker setup
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── main.py                 # Entry point for the application
```

---

## Prerequisites

1. **Python 3.11 or later**
2. **Vosk Model**: Download and place the model in the `model` directory.
3. **API Keys**:
   - OpenAI API Key
   - Whisper API Key (Optional)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sattyamjjain/AgentX.git
   cd AgentX
   ```

2. Set up the environment:

   ```bash
   ./scripts/setup_env.sh
   ```

3. Create a `.env` file:

   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key>
   WHISPER_API_KEY=<your_whisper_api_key>
   DEBUG=True
   ```

4. Run the application:

   ```bash
   python3 main.py
   ```

---

## Testing

Run the test suite using `pytest`:

```bash
pytest tests/
```

---

## Usage

1. **Running the Agent**:
   ```bash
   python3 main.py
   ```

2. **Interactive Voice Commands**:
   - Speak into the microphone, and AgentX will respond.

3. **Document Retrieval**:
   - Place `.txt` files in `data/documents` to make them available for querying.

---

## Future Enhancements

1. **Integration with Whisper API** for high-quality transcription.
2. **Multi-modal capabilities** for image and video processing.
3. **Improved conversational flows** with dynamic memory management.

---

## Contributors

- [Sattyam Jain](https://github.com/sattyamjjain)
- Open to contributions!

---

## Support

For issues or feature requests, please open an issue on the [GitHub repository](<repository_url>).
