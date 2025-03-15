import argparse
import warnings
import sys
from src.models.vector_store import VectorStore
from src.models.response_generator import generate_response
from src.parsers.markdown_loader import MarkdownLoader
from src.config import Config

# Filtrer les avertissements de dépréciation de LangChain
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*This class is deprecated.*")
warnings.filterwarnings("ignore", message=".*The method.*was deprecated.*")

# Rediriger stderr vers null pour supprimer les avertissements restants
class NullWriter:
    def write(self, text):
        pass

def main():
    """
    Interface en ligne de commande pour interagir avec le système RAG.
    """
    # Sauvegarder stderr original
    original_stderr = sys.stderr
    
    try:
        # Configuration du parseur d'arguments
        parser = argparse.ArgumentParser(
            description="RAG - Système de questions-réponses sur les documents",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        # Ajout des arguments
        parser.add_argument(
            "--document",
            "-d",
            type=str,
            required=True,
            help="Nom du document à analyser (ex: balance_commerciale_2020-1)"
        )

        parser.add_argument(
            "--question",
            "-q",
            type=str,
            required=True,
            help="Question à poser sur le document"
        )

        # Parsing des arguments
        args = parser.parse_args()

        # Rediriger stderr vers null pendant l'exécution
        sys.stderr = NullWriter()

        # Chargement du document
        print(f"\nChargement du document '{args.document}'...")
        markdown_text = MarkdownLoader.load_markdown(args.document)
        
        # Construction de l'index vectoriel
        print("Construction de l'index vectoriel...")
        vector_store = VectorStore()
        vector_store.build_index(markdown_text)
        
        # Génération de la réponse
        print("\nGénération de la réponse...\n")
        response = generate_response(args.question, vector_store, Config.GOOGLE_API_KEY)
        
        # Affichage des résultats
        print("\n" + "="*80)
        print(f"Question : {args.question}")
        print("="*80)
        print(f"\nRéponse :\n{response}")
        print("="*80 + "\n")

    except Exception as e:
        print(f"\nErreur : {str(e)}")
        return 1
    finally:
        # Restaurer stderr original
        sys.stderr = original_stderr

    return 0

if __name__ == "__main__":
    exit(main())
