import os
import nest_asyncio
from llama_cloud_services import LlamaParse

import sys
import os

# Ajouter le dossier "src" au chemin d'importation
sys.path.append(os.path.abspath("src"))

# Maintenant, on peut importer
from config import Config 

nest_asyncio.apply()

class LlamaParser:
    def __init__(self, api_key, result_type="markdown", num_workers=4, language="en", parsing_instruction=None):
        self.parser = LlamaParse(
            api_key=api_key,
            result_type=result_type,
            num_workers=num_workers,
            language=language,
            parsing_instruction=parsing_instruction
        )

    def parse_and_save(self, file_path, output_path="src/parsers/results/output.md"):
        """
        Analyse un document et enregistre directement le résultat en Markdown.
        
        :param file_path: Chemin du fichier à analyser.
        :param output_path: Chemin du fichier de sortie.
        """
        # Analyse du document
        documents = self.parser.load_data(file_path)
        
        # Création du dossier de sortie s'il n'existe pas
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        # Enregistrement du résultat en Markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            for doc in documents:
                f.write(doc.text + "\n")



api_key = Config.LLAMA_CLOUD_API_KEY  # Remplacer par votre clé d'API

# # Instanciation de la classe LlamaParser avec les paramètres souhaités
parser = LlamaParser(
     api_key=api_key,
     result_type="markdown",
     num_workers=4,
     language="en",
     parsing_instruction=None
 )

# # Appel de la méthode unique qui parse le document et l'enregistre en Markdown
parser.parse_and_save(r"data\balance_commerciale_2020-1.pdf", "src/parsers/results/balance_commerciale_2020-1.md")
# parser.parse_and_save("data\BF-Etats-financiers-2020.pdf", "src/parsers/results/BF-Etats-financiers-2020.md")
# parser.parse_and_save("data\BURKINA FASO_Constitution.pdf", "src/parsers/results/BURKINA FASO_Constitution.md")
