import os
from dotenv import load_dotenv
from enum import Enum

# Chargement des variables d'environnement
load_dotenv()

# Clé API Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Types d'interlocuteurs dans le chat
class SPEAKER_TYPES(str, Enum):
    USER = "user"
    BOT = "assistant"

# Message initial du chatbot
initial_prompt = {
    "role": SPEAKER_TYPES.BOT,
    "content": "Bonjour ! Je suis votre assistant virtuel spécialisé dans l'analyse des rapports de solvabilité. Comment puis-je vous aider aujourd'hui ?"
} 