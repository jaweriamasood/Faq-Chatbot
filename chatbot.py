import string
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load English tokenizer
nlp = spacy.load("en_core_web_sm")

faq_data = {
    "What is your return policy?": "We accept returns within 30 days of purchase.",
    "How long is the warranty?": "All products come with a 1-year warranty.",
    "Do you offer international shipping?": "Yes, we ship worldwide with standard and express options.",
    "How can I track my order?": "You can track your order using the tracking number provided via email.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and Apple Pay."
}

def preprocess(text):
    doc = nlp(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return " ".join([token.text for token in doc if not token.is_stop])

questions = list(faq_data.keys())
preprocessed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(preprocessed_questions)

def get_faq_response(user_input):
    user_input_clean = preprocess(user_input)
    user_vector = vectorizer.transform([user_input_clean])
    similarities = cosine_similarity(user_vector, faq_vectors)
    index = np.argmax(similarities)
    score = similarities[0][index]

    if score < 0.3:
        return "❌ Sorry, I couldn't find a relevant answer."
    return faq_data[questions[index]]


