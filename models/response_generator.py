from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

class ResponseGenerator:
    def __init__(self, api_key, model_name="gemini-1.5-flash"):
        self.model = ChatGoogleGenerativeAI(model=model_name, temperature=0.3, api_key=api_key)
        self.prompt_template = PromptTemplate(
            template=self._get_prompt_template(), 
            input_variables=['context', 'question']
        )

    def _get_prompt_template(self):
        return """
        Tu es un expert en analyse financière , en droit et loi juridique et en e commerce .Tu seras chargé d'analyser des contenus dans ses documents et de répondre à des questions en utilisant tes connaissances.

        Contexte:\n{context}\n

        Question:\n{question}\n

        Réponds de manière détaillée et analytique :
        """

    def generate_response(self, question, vector_index):
        docs = vector_index.search(question)
        chain = load_qa_chain(self.model, chain_type="stuff", prompt=self.prompt_template)
        response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
        return response['output_text']
