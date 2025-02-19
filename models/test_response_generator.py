# Replace with your actual API key and vector index setup
from response_generator import ResponseGenerator

# Remplacer par votre véritable clé API
api_key = ""

# Créer une instance de ResponseGenerator
response_generator = ResponseGenerator(api_key=api_key)

# Exemple de question
question = "Quelles sont les dernières tendances du commerce électronique ?"

# Générer la réponse
response = response_generator.generate_response(question, vector_index=None)

# Afficher la réponse générée
print(response)

