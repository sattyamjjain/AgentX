import os
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from gtts import gTTS
from playsound import playsound

from config.constants import VOSK_MODEL_DIR
from utils.logger import get_logger

logger = get_logger("VoiceProcessor")


class VoiceProcessor:
    def __init__(self, model_path=VOSK_MODEL_DIR):
        if not os.path.exists(model_path):
            logger.error(f"Model not found at {model_path}")
            raise FileNotFoundError(f"Model not found at {model_path}")
        self.model = Model(model_path)
        self.audio_queue = queue.Queue()
        logger.info("VoiceProcessor initialized successfully.")

    def record_audio(self):
        recognizer = KaldiRecognizer(self.model, 16000)
        logger.info("Listening... Speak now.")
        print("Listening... Speak now. Say 'exit' to quit.")

        def audio_callback(indata, frames, time, status):
            if status:
                logger.error(f"Audio input error: {status}")
            self.audio_queue.put(bytes(indata))

        try:
            with sd.InputStream(
                callback=audio_callback, channels=1, samplerate=16000, dtype="int16"
            ):
                while True:
                    data = self.audio_queue.get()
                    if recognizer.AcceptWaveform(data):
                        result = recognizer.Result()
                        text = eval(result).get("text", "")
                        logger.info(f"Transcription: {text}")
                        return text
        except Exception as e:
            logger.error(f"Audio recording error: {e}")
            return ""

    def text_to_speech(self, text):
        logger.info(f"Converting text to speech: {text}")
        tts = gTTS(text)
        output_path = "response.mp3"
        try:
            tts.save(output_path)
            playsound(output_path)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)
                logger.info("Temporary audio file deleted.")
