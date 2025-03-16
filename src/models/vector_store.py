from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
import os, sys, nest_asyncio,faiss

# Ajouter le dossier "src" au chemin d'importation
sys.path.append(os.path.abspath("src"))

# Maintenant, on peut importer
from config import Config 

nest_asyncio.apply()

class VectorStore:
    def __init__(self):
        """Initialise le stockage vectoriel avec les embeddings Google."""
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=Config.GOOGLE_API_KEY
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.index = None
        self.texts = []

    def build_index(self, text: str):
        """
        Construit l'index vectoriel à partir du texte fourni.
        
        Args:
            text (str): Texte à indexer
        """
        # Découpage du texte en chunks
        self.texts = self.text_splitter.split_text(text)
        
        # Création des embeddings
        embeddings = self.embeddings.embed_documents(self.texts)
        
        # Création de l'index FAISS
        dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)
        
        # Ajout des vecteurs à l'index
        self.index.add(np.array(embeddings))

    def similarity_search(self, query: str, k: int = 4) -> List[str]:
        """
        Recherche les k passages les plus similaires à la requête.
        
        Args:
            query (str): Requête de recherche
            k (int): Nombre de résultats à retourner
            
        Returns:
            List[str]: Liste des k passages les plus similaires
        """
        if not self.index:
            raise ValueError("L'index n'a pas été construit. Appelez build_index() d'abord.")
            
        # Création de l'embedding de la requête
        query_embedding = self.embeddings.embed_query(query)
        
        # Recherche des k plus proches voisins
        distances, indices = self.index.search(np.array([query_embedding]), k)
        
        # Retourne les textes correspondants
        return [self.texts[i] for i in indices[0]]
