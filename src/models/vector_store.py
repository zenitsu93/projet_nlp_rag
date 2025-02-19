from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter


class VectorStore:
    """
    Classe pour gérer l'index FAISS à partir d'un texte donné.
    """

    def __init__(self, model_name="models/embedding-001"):
        """
        Initialise le modèle d'embedding.
        """
        self.model_name = model_name
        self.embeddings = GoogleGenerativeAIEmbeddings(model=model_name)
        self.vectorstore = None

    def initialize_faiss_index(self, text, chunk_size=100000, chunk_overlap=200):
        """
        Crée un index FAISS à partir du texte fourni.
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split_text(text)
        self.vectorstore = FAISS.from_texts(texts, self.embeddings)
        return self.vectorstore

    def search(self, query, top_k=5):
        """
        Recherche les documents les plus similaires à la requête.
        """
        if self.vectorstore is None:
            raise ValueError("L'index FAISS n'est pas encore initialisé.")
        return self.vectorstore.similarity_search(query, k=top_k)
