import re
import spacy
import os

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

class TextAnalyzer:
    def __init__(self, stopwords, positive_words, negative_words):
        self.stopwords = stopwords
        self.positive_words = positive_words
        self.negative_words = negative_words

    def clean_text(self, text):

        text = re.sub(r'[^\w\s]', '', text) 
        words = text.split()
        return [word.lower() for word in words if word.lower() not in self.stopwords]

    def analyze(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            raw_text = file.read()

        cleaned_words = self.clean_text(raw_text)
        cleaned_text = " ".join(cleaned_words)
        doc = nlp(cleaned_text)

        word_count = len(cleaned_words)
        sentence_count = len(list(doc.sents))
        complex_word_count = sum(1 for word in cleaned_words if sum(1 for char in word if char in 'aeiouAEIOU') > 2)
        syllable_count = sum(sum(1 for char in word if char in 'aeiouAEIOU') for word in cleaned_words)
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        percentage_complex_words = (complex_word_count / word_count) * 100 if word_count > 0 else 0
        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

        positive_score = sum(1 for word in cleaned_words if word in self.positive_words)
        negative_score = sum(1 for word in cleaned_words if word in self.negative_words)
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)

        personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', raw_text, re.IGNORECASE))
        avg_word_length = sum(len(word) for word in cleaned_words) / word_count if word_count > 0 else 0

        return {
            "POSITIVE SCORE": positive_score,
            "NEGATIVE SCORE": negative_score,
            "POLARITY SCORE": polarity_score,
            "SUBJECTIVITY SCORE": subjectivity_score,
            "AVG SENTENCE LENGTH": avg_sentence_length,
            "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
            "FOG INDEX": fog_index,
            "AVG NUMBER OF WORDS PER SENTENCE": avg_sentence_length,
            "COMPLEX WORD COUNT": complex_word_count,
            "WORD COUNT": word_count,
            "SYLLABLE PER WORD": syllable_count / word_count if word_count > 0 else 0,
            "PERSONAL PRONOUNS": personal_pronouns,
            "AVG WORD LENGTH": avg_word_length,
        }
