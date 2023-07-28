# ai/nlp.py

import nltk
import spacy

nlp = spacy.load('en_core_web_sm')

def process_text(text):
    doc = nlp(text)
    # Here we can do various NLP tasks on the text, like tokenization, lemmatization, part-of-speech tagging, etc.
    # For now, let's just return the lemmatized form of the words.
    return [token.lemma_ for token in doc]
