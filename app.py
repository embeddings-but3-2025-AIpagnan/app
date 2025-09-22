from flask import Flask, render_template, request, jsonify, flash
import re
import random

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'

@app.route("/")
def home():
    """Page d'accueil avec présentation des fonctionnalités"""
    return render_template('index.html')

@app.route("/chat")
def chat():
    """Interface de chat conversationnel"""
    return render_template('chat.html')

@app.route("/analyze")
def analyze():
    """Interface d'analyse de texte"""
    return render_template('analyze.html')

@app.route("/api/chat", methods=['POST'])
def api_chat():
    """API endpoint pour le chat - simulation d'un LLM simple"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'success': False, 'error': 'Message vide'})
        
        # Simulation de réponses intelligentes basiques
        response = generate_chat_response(message)
        
        return jsonify({'success': True, 'response': response})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/api/analyze", methods=['POST'])
def api_analyze():
    """API endpoint pour l'analyse de texte"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        analysis_type = data.get('analysis_type', '')
        
        if not text or not analysis_type:
            return jsonify({'success': False, 'error': 'Données manquantes'})
        
        result = analyze_text(text, analysis_type)
        
        return jsonify({'success': True, 'result': result})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def generate_chat_response(message):
    """Génère une réponse de chat basique simulant un LLM"""
    message_lower = message.lower()
    
    # Réponses basées sur des mots-clés
    if any(word in message_lower for word in ['bonjour', 'salut', 'hello', 'bonsoir']):
        responses = [
            "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
            "Salut ! Je suis votre assistant IA. Que puis-je faire pour vous ?",
            "Bonjour ! Je suis là pour répondre à vos questions."
        ]
    elif any(word in message_lower for word in ['merci', 'thank']):
        responses = [
            "De rien ! N'hésitez pas si vous avez d'autres questions.",
            "Je suis content d'avoir pu vous aider !",
            "C'est un plaisir de vous aider !"
        ]
    elif any(word in message_lower for word in ['comment', 'aide', 'help']):
        responses = [
            "Je peux vous aider avec diverses tâches comme répondre à des questions, analyser du texte, ou discuter de sujets divers. Que souhaitez-vous faire ?",
            "Je suis un assistant IA capable de répondre à vos questions et d'analyser du texte. Comment puis-je vous assister ?",
            "Posez-moi une question ou utilisez la section analyse pour traiter du texte !"
        ]
    elif any(word in message_lower for word in ['qui', 'what', 'qu\'est-ce']):
        responses = [
            "Je suis un assistant IA développé pour cette application Flask. Je peux répondre à vos questions et analyser du texte.",
            "Je suis votre assistant virtuel, conçu pour vous aider avec diverses tâches de traitement de texte et de conversation.",
            "Je suis une simulation d'IA créée pour démontrer les fonctionnalités basiques d'un assistant conversationnel."
        ]
    elif '?' in message:
        responses = [
            "C'est une question intéressante ! Basé sur ce que je comprends, je dirais que cela dépend du contexte spécifique.",
            "Pour répondre à votre question, il me faudrait plus de détails, mais voici ce que je peux vous dire en général...",
            "Excellente question ! Laissez-moi réfléchir à la meilleure façon de vous répondre.",
            "Je vais faire de mon mieux pour répondre à votre question basée sur mes connaissances actuelles."
        ]
    else:
        responses = [
            "Intéressant ! Pouvez-vous me donner plus de détails sur ce sujet ?",
            "Je comprends votre point. Qu'aimeriez-vous savoir de plus à ce sujet ?",
            "C'est un sujet fascinant ! Avez-vous des questions spécifiques à ce propos ?",
            "Merci pour cette information. Comment puis-je vous aider davantage ?",
            "Je vois ! Y a-t-il quelque chose de spécifique que vous aimeriez explorer sur ce sujet ?"
        ]
    
    return random.choice(responses)

def analyze_text(text, analysis_type):
    """Analyse le texte selon le type demandé"""
    if analysis_type == 'summary':
        return generate_summary(text)
    elif analysis_type == 'sentiment':
        return analyze_sentiment(text)
    elif analysis_type == 'keywords':
        return extract_keywords(text)
    elif analysis_type == 'length':
        return calculate_text_stats(text)
    else:
        return "Type d'analyse non supporté"

def generate_summary(text):
    """Génère un résumé basique du texte"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= 2:
        return "Le texte est déjà court. Résumé : " + text[:200] + "..."
    
    # Prendre les premières et dernières phrases pour un résumé basique
    summary_sentences = []
    if len(sentences) > 0:
        summary_sentences.append(sentences[0])
    if len(sentences) > 2:
        summary_sentences.append(sentences[-1])
    
    summary = " ".join(summary_sentences)
    return f"Résumé automatique (basique) : {summary}"

def analyze_sentiment(text):
    """Analyse basique du sentiment"""
    positive_words = ['bon', 'bien', 'excellent', 'super', 'génial', 'parfait', 'merveilleux', 'fantastique', 'positif', 'heureux', 'content']
    negative_words = ['mauvais', 'mal', 'horrible', 'terrible', 'nul', 'décevant', 'négatif', 'triste', 'en colère', 'frustré']
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        return "Sentiment positif détecté"
    elif negative_count > positive_count:
        return "Sentiment négatif détecté"
    else:
        return "Sentiment neutre"

def extract_keywords(text):
    """Extraction basique de mots-clés"""
    # Mots vides français courants
    stop_words = {'le', 'de', 'et', 'à', 'un', 'il', 'être', 'et', 'en', 'avoir', 'que', 'pour', 'dans', 'ce', 'son', 'une', 'sur', 'avec', 'ne', 'se', 'pas', 'tout', 'plus', 'par', 'grand', 'en', 'le', 'la', 'les', 'des', 'du', 'un', 'une', 'est', 'qui', 'que', 'où', 'comment', 'quand', 'ou', 'mais', 'donc'}
    
    # Nettoyer et diviser le texte
    words = re.findall(r'\b[a-zA-ZÀ-ÿ]{3,}\b', text.lower())
    
    # Filtrer les mots vides et compter les occurrences
    word_freq = {}
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Retourner les mots les plus fréquents
    keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    return [word for word, freq in keywords]

def calculate_text_stats(text):
    """Calcule les statistiques du texte"""
    characters = len(text)
    words = len(text.split())
    sentences = len(re.split(r'[.!?]+', text)) - 1  # -1 car split ajoute un élément vide à la fin
    paragraphs = len([p for p in text.split('\n') if p.strip()])
    
    return {
        'characters': characters,
        'words': words,
        'sentences': max(1, sentences),  # Au moins 1 phrase
        'paragraphs': max(1, paragraphs)  # Au moins 1 paragraphe
    }

if __name__ == "__main__":
    app.run(debug=True)
