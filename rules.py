import re

# Predefined 10 technical questions
rules = {
    "what is python": "Python is a high-level programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning allows systems to learn from data.",
    "what is deep learning": "Deep Learning uses neural networks.",
    "what is flask": "Flask is a lightweight Python web framework.",
    "what is api": "API allows applications to communicate.",
    "what is html": "HTML structures web pages.",
    "what is css": "CSS styles web pages.",
    "what is javascript": "JavaScript makes web pages interactive.",
    "what is database": "A database stores structured information."
}

def chatbot_reply(message):
    """
    Returns correct response for exact matching message.
    """
    message = message.lower().strip()
    for question, answer in rules.items():
        if re.fullmatch(re.escape(question), message):
            return answer
    return "Please ask one of the predefined technical questions."
