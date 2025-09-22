# Application LLM Flask

Une application web en Python Flask permettant d'implémenter les fonctionnalités intelligentes du LLM (Large Language Model).

## Fonctionnalités

### 💬 Chat Intelligent
- Interface de conversation interactive
- Réponses intelligentes basées sur l'analyse de mots-clés
- Interface utilisateur moderne avec bulles de messages
- Communication en temps réel via AJAX

### 📊 Analyse de Texte
- **Résumé automatique** : Génération de résumés à partir de textes longs
- **Analyse de sentiment** : Détection du sentiment positif, négatif ou neutre
- **Extraction de mots-clés** : Identification des termes les plus importants
- **Statistiques de texte** : Comptage des caractères, mots, phrases et paragraphes

### 🎨 Interface Web
- Design responsive utilisant Bootstrap 5
- Navigation intuitive entre les fonctionnalités
- Interface moderne et professionnelle
- Compatible mobile et desktop

## Installation

1. Cloner le repository :
```bash
git clone <repository-url>
cd app
```

2. Créer un environnement virtuel :
```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur Linux/Mac
# ou
.venv\Scripts\activate     # Sur Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancer l'application :
```bash
python app.py
```

2. Ouvrir votre navigateur et aller à :
```
http://127.0.0.1:5000
```

3. Explorer les fonctionnalités :
   - **Accueil** : Vue d'ensemble des fonctionnalités
   - **Chat** : Interface conversationnelle
   - **Analyse** : Outils d'analyse de texte

## API Endpoints

### Chat API
- **URL** : `/api/chat`
- **Méthode** : POST
- **Format** : JSON
```json
{
  "message": "Votre message ici"
}
```

### Analyse API
- **URL** : `/api/analyze`
- **Méthode** : POST
- **Format** : JSON
```json
{
  "text": "Texte à analyser",
  "analysis_type": "summary|sentiment|keywords|length"
}
```

## Structure du Projet

```
app/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── templates/            # Templates HTML
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── chat.html         # Interface de chat
│   └── analyze.html      # Interface d'analyse
└── static/              # Fichiers statiques
    ├── css/
    │   └── style.css     # Styles personnalisés
    └── js/
        └── main.js       # JavaScript personnalisé
```

## Technologie

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Communication** : AJAX/REST API
- **Responsive Design** : Bootstrap Grid System

## Développement

Cette application fournit une base solide pour l'implémentation de fonctionnalités LLM plus avancées. Elle peut être étendue avec :

- Intégration d'APIs LLM réelles (OpenAI, Hugging Face, etc.)
- Base de données pour la persistance des conversations
- Authentification utilisateur
- Fonctionnalités d'analyse de texte plus sophistiquées
- Support multilingue

## Licence

Projet éducatif - À adapter selon vos besoins.
