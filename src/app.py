import streamlit as st
#from config import GOOGLE_API_KEY, SPEAKER_TYPES, initial_prompt
from config import Config, SPEAKER_TYPES, initial_prompt
from models.vector_store import VectorStore
from models.response_generator import generate_response
from parsers.markdown_loader import MarkdownLoader

def main():
    """
    Application RAG : Rapports sur la Solvabilité et la Situation Financière
    """
    # Configuration de la page Streamlit
    st.set_page_config(
        page_title="RAG - Rapports sur la Solvabilité",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialisation des variables de session si elles n'existent pas
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [initial_prompt]
    if 'selected_text' not in st.session_state:
        st.session_state.selected_text = None
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None

    # Barre latérale
    with st.sidebar:
        st.title("📊 RAG - Rechercher vos informations facilement")
        st.button("Effacer l'historique", on_click=lambda: st.session_state.update(chat_history=[initial_prompt]))

        # Sélection de la compagnie d'assurance / du document
        st.subheader("Choisissez le document :")
        documents = {
            "balance_commerciale_2020-1": st.checkbox("balance_commerciale_2020-1"),
            "BF-Etats-financiers-2020": st.checkbox("BF-Etats-financiers-2020"),
            "BURKINA FASO_Constitution": st.checkbox("BURKINA FASO_Constitution"),
        }

        selected_docs = [name for name, selected in documents.items() if selected]

        if len(selected_docs) == 1:
            new_doc = selected_docs[0]
            # Réinitialisation de l'historique et du vector_store si le document a changé
            if st.session_state.get("selected_text") != new_doc:
                st.session_state.chat_history = [initial_prompt]
                st.session_state.vector_store = None
            st.session_state.selected_text = new_doc
            st.success(f"Document sélectionné : {st.session_state.selected_text}")
        elif len(selected_docs) > 1:
            st.warning("Veuillez sélectionner un seul document.")
            st.session_state.selected_text = None
        else:
            st.warning("Aucun document n'a été sélectionné.")
            st.session_state.selected_text = None

        # Initialisation du vector store si un document est sélectionné
        if st.session_state.selected_text and not st.session_state.vector_store:
            with st.spinner("Chargement des données..."):
                markdown_text = MarkdownLoader.load_markdown(st.session_state.selected_text)
                vector_store = VectorStore()
                vector_store.build_index(markdown_text)
                st.session_state.vector_store = vector_store
                st.success("Données chargées avec succès !")

    # Interface principale
    st.header("💬 Chatbot")
    if not st.session_state.selected_text:
        st.warning("Veuillez sélectionner un document.")
        return

    # Interface de chat
    st.write("Posez vos questions sur le rapport sélectionné :")
    prompt = st.chat_input("Entrez une question :", key="user_input")
    
    if prompt:
        with st.spinner("Génération de la réponse..."):
            response = generate_response(prompt, st.session_state.vector_store, Config.GOOGLE_API_KEY)
            
            st.session_state.chat_history.append({"role": SPEAKER_TYPES.USER, "content": prompt})
            st.session_state.chat_history.append({"role": SPEAKER_TYPES.BOT, "content": response})

        # Affichage des messages de chat
        for message in st.session_state.chat_history:
            if message["role"] == SPEAKER_TYPES.USER:
                st.chat_message(SPEAKER_TYPES.USER, avatar="👤").write(message["content"])
            else:
                st.chat_message(SPEAKER_TYPES.BOT, avatar="📊").write(message["content"])

    # Footer
    st.markdown("""
    <hr>
    <div style="text-align: center;">
        <small>RAG Application - Discutez aisément avec vos documents</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
