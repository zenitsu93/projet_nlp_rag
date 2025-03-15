# 🤖 RAG - Système de Questions-Réponses sur Documents

## 📝 Description

RAG (Retrieval-Augmented Generation) est un système intelligent de questions-réponses qui permet d'interagir naturellement avec vos documents. Il combine la puissance du traitement du langage naturel et de la recherche sémantique pour fournir des réponses précises basées sur le contenu de vos documents.

## ✨ Fonctionnalités

- 🔍 Recherche sémantique avancée
- 💬 Interface conversationnelle intuitive
- 📊 Support des documents Markdown
- 🚀 Double interface : Web (Streamlit) et CLI
- 🔄 Mise à jour en temps réel des réponses
- 🎯 Réponses contextuelles précises

## 🛠️ Technologies Utilisées

- **Python 3.8+**
- **Streamlit** : Interface utilisateur web
- **LangChain** : Framework pour les applications LLM
- **FAISS** : Indexation et recherche vectorielle
- **Google Gemini Pro** : Modèle de langage
- **HuggingFace** : Embeddings de texte

## 📋 Prérequis

- Python 3.8 ou supérieur
- Clé API Google (pour Gemini Pro)
- pip (gestionnaire de paquets Python)

## ⚙️ Installation

1. Clonez le dépôt :
```bash
git clone [url-du-repo]
cd [nom-du-repo]
```

2. Créez et activez un environnement virtuel :
```bash
python -m venv env
source env/bin/activate  # Linux/MacOS
# ou
env\\Scripts\\activate  # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez vos variables d'environnement :
```bash
# Créez un fichier .env à la racine du projet
GOOGLE_API_KEY=votre_clé_api_google
```

## 🚀 Utilisation

### Interface Web (Streamlit)

1. Lancez l'application :
```bash
streamlit run src/app.py
```

2. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501)

3. Sélectionnez un document dans la barre latérale et posez vos questions !

### Interface CLI

Pour une utilisation en ligne de commande :

```bash
python cli.py -d [nom_du_document] -q "Votre question ici"
```

Exemple :
```bash
python cli.py -d balance_commerciale_2020-1 -q "Quelle est la balance commerciale en 2020 ?"
```

## 📁 Structure du Projet

```
.
├── src/
│   ├── app.py                    # Application Streamlit
│   ├── config/
│   │   └── globals.py           # Configuration globale
│   ├── models/
│   │   ├── vector_store.py      # Gestion des embeddings et recherche
│   │   └── response_generator.py # Génération des réponses
│   └── parsers/
│       └── markdown_loader.py    # Chargement des documents
├── data/
│   └── markdown/                 # Documents source
├── cli.py                        # Interface en ligne de commande
├── requirements.txt              # Dépendances du projet
└── README.md                     # Documentation
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez votre branche de fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- [Votre Nom] - *Développement initial*

## 📫 Contact

Pour toute question ou suggestion, n'hésitez pas à :
- Ouvrir une issue
- Envoyer un email à [votre-email]
- [Autres moyens de contact]

## 🙏 Remerciements

- Google pour l'API Gemini Pro
- L'équipe Streamlit pour leur excellent framework
- La communauté LangChain pour leurs outils et leur support

