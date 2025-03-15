
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

def generate_response(question, vector_index, api_key, model_name="gemini-1.5-flash"):
    """
    Génère une réponse à partir de la question et du contexte fourni par l'index vectoriel.
    """
    docs = vector_index.search(question)
    prompt_template =  """
        Tu es un expert universel doté d'une expertise approfondie dans tous les domaines. 
        Ta mission est de répondre aux questions de l'utilisateur en te basant **exclusivement** sur le contexte fourni. 
        Ne fais aucune supposition en dehors du contexte et adopte une approche factuelle et analytique.

        🔹 **Contexte disponible** :
        {context}

        🔹 **Question de l'utilisateur** :
        {question}

        🔹 **Instructions pour ta réponse** :
        - Fournis une réponse détaillée et bien structurée.
        - Analyse la question en profondeur et propose des explications claires.
        - Si nécessaire, divise ta réponse en sections pour une meilleure lisibilité.
        - Reste concis et pertinent : ne donne pas d’informations inutiles.
        - Si le contexte ne permet pas de répondre précisément, mentionne-le plutôt que d'inventer une réponse.

        ✅ Réponds maintenant :
        """
    
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
    model = ChatGoogleGenerativeAI(model=model_name, temperature=0.3, api_key=api_key)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
    return response['output_text']