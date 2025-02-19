import os

class MarkdownLoader:
    @staticmethod
    def load_markdown(file_path):
        """
        Charge le contenu d'un fichier Markdown depuis un chemin donné et retourne le fichier et son contenu.
        
        :param file_path: Chemin d'accès au fichier Markdown
        :return: Tuple contenant le fichier et son contenu
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'a pas été trouvé.")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return file_path, content
        except Exception as e:
            raise Exception(f"Erreur lors de la lecture du fichier: {str(e)}")
