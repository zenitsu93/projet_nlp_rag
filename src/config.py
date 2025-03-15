import os

class Config:
    LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Global variables
class SPEAKER_TYPES:
  USER = "user"
  BOT = "bot"


initial_prompt = {"role": SPEAKER_TYPES.BOT, "content": "Comment puis je vous aider aujourd'hui?"}

