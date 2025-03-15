from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

class VectorStore:
    def __init__(self, model_name="models/embedding-001", chunk_size=100000, chunk_overlap=200):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.embeddings = GoogleGenerativeAIEmbeddings(model=model_name)
        self.vectorstore = None

    def build_index(self, text):
        texts = self.text_splitter.split_text(text)
        self.vectorstore = FAISS.from_texts(texts, self.embeddings)

    def search(self, query):
        if self.vectorstore is None:
            raise ValueError("L'index FAISS n'a pas été initialisé.")
        return self.vectorstore.similarity_search(query)
