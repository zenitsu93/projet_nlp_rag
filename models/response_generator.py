from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
import faiss
import numpy as np

class ResponseGenerator:
    def __init__(self, api_key, model_name="gemini-1.5-flash"):
        self.model = ChatGoogleGenerativeAI(model=model_name, temperature=0.3, api_key=api_key)
        self.prompt_template = PromptTemplate(
            template=self._get_prompt_template(), 
            input_variables=['context', 'question']
        )

        # Initialisation de l'index vectoriel (exemple FAISS)
        self.index = self._initialize_vector_index()

    def _get_prompt_template(self):
        return """
        Tu es un expert en analyse financière , en droit et loi juridique et en e commerce .Tu seras chargé d'analyser des contenus dans ses documents et de répondre à des questions en utilisant tes connaissances.

        Contexte:\n{context}\n

        Question:\n{question}\n

        Réponds de manière détaillée et analytique :
        """

    def _initialize_vector_index(self):
        # Exemple : initialisation de FAISS avec des embeddings de documents aléatoires
        document_embeddings = np.random.rand(10, 128).astype('float32')  # 10 documents avec 128 dimensions
        index = faiss.IndexFlatL2(128)
        index.add(document_embeddings)
        return index

    def generate_response(self, question, vector_index=None):
        # Supposons que vous avez une fonction qui génère des embeddings pour la question
        question_embedding = np.random.rand(128).astype('float32')  # Remplaçant pour l'embedding réel de la question

        # Recherche dans l'index pour les documents pertinents
        distances, indices = self.index.search(np.array([question_embedding], dtype='float32'), k=3)

        # Obtenez les documents correspondant aux indices
        docs = self._get_documents_by_indices(indices[0])  # indices[0] pour accéder à la première ligne des résultats

        # Charger la chaîne QA
        chain = load_qa_chain(self.model, chain_type="stuff", prompt=self.prompt_template)
        response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
        return response['output_text']

    def _get_documents_by_indices(self, indices):
        # Aplatir les indices pour un accès 1D
        indices = indices.flatten()  # Assurez-vous que c'est un tableau 1D

        # Simuler des documents avec du contenu et des métadonnées
        documents = [
            Document(page_content="Contenu du document 1", metadata={"source": "source1"}),
            Document(page_content="Contenu du document 2", metadata={"source": "source2"}),
            Document(page_content="Contenu du document 3", metadata={"source": "source3"}),
            Document(page_content="Contenu du document 4", metadata={"source": "source4"}),
            Document(page_content="Contenu du document 5", metadata={"source": "source5"}),
            Document(page_content="Contenu du document 6", metadata={"source": "source6"}),
            Document(page_content="Contenu du document 7", metadata={"source": "source7"}),
            Document(page_content="Contenu du document 8", metadata={"source": "source8"}),
            Document(page_content="Contenu du document 9", metadata={"source": "source9"}),
            Document(page_content="Contenu du document 10", metadata={"source": "source10"})
        ]
        
        # Retourner les documents en fonction des indices
        return [documents[i] for i in indices]
