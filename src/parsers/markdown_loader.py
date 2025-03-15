import os
from pathlib import Path

class MarkdownLoader:
    @staticmethod
    def load_markdown(company_name: str) -> str:
        """
        Charge le contenu du fichier Markdown correspondant à la compagnie d'assurance.
        
        Args:
            company_name (str): Nom de la compagnie d'assurance
            
        Returns:
            str: Contenu du fichier Markdown
        """
        # Chemin vers le dossier des données
        #data_dir = Path('src\parsers\results')

        # Correct way to define a cross-platform path
        data_dir = Path("src") / "parsers" / "results"


        # Construction du chemin du fichier
        filename = f"{company_name}.md"
        file_path = data_dir / filename
        
        try:
            if not file_path.exists():
                raise FileNotFoundError(f"Le fichier {filename} n'existe pas dans {data_dir}")
                
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
                
        except Exception as e:
            raise Exception(f"Erreur lors du chargement du fichier {filename}: {str(e)}")
