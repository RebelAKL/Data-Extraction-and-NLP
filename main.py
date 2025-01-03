import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
import re


def load_word_list(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        words = file.read().splitlines()
    return set(words)

positive_words = load_word_list("MasterDictionary\\positive-words.txt")
negative_words = load_word_list("MasterDictionary\\negative-words.txt")

def analyze_text(text): 

    nlp = spacy.load("en_core_web_sm") 
    doc = nlp(text)

    word_count = len([token for token in doc if not token.is_space])
    sentence_count = len(list(doc.sents))

    positive_score = sum(1 for token in doc if token.text.lower() in positive_words)
    negative_score = sum(1 for token in doc if token.text.lower() in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 1e-6)
    subjectivity_score = (positive_score + negative_score) / (word_count + 1e-6)
    avg_sentence_length = word_count / sentence_count if sentence_count != 0 else 0

    def syllable_count(word):
        return len(re.findall(r'[aeiouy]+', word.lower()))

    complex_words = [token.text for token in doc if syllable_count(token.text) > 2]
    complex_word_count = len(complex_words)
    percentage_complex_words = (complex_word_count / word_count) * 100 if word_count != 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_word_length = sum(len(token.text) for token in doc) / word_count if word_count != 0 else 0
    syllables_per_word = sum(syllable_count(token.text) for token in doc) / word_count if word_count != 0 else 0
    personal_pronouns = len([token for token in doc if token.text.lower() in ["i", "we", "my", "ours", "us"]]) 

    return {
        "Positive Score": positive_score,
        "Negative Score": negative_score,
        "Polarity Score": polarity_score,
        "Subjectivity Score": subjectivity_score,
        "Avg Sentence Length": avg_sentence_length,
        "Percentage of Complex Words": percentage_complex_words,
        "Fog Index": fog_index,
        "Complex Word Count": complex_word_count,
        "Word Count": word_count,
        "Syllable Per Word": syllables_per_word,
        "Personal Pronouns": personal_pronouns,
        "Avg Word Length": avg_word_length
    }

def extract_articles(input_file):
    df = pd.read_excel(input_file)
    os.makedirs("articles", exist_ok=True)

    for index, row in df.iterrows():
        url_id = row["URL_ID"]
        url = row["URL"]
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1').get_text(strip=True)
            article_body = soup.find('article').get_text(strip=True)
            
            with open(f"articles/{url_id}.txt", "w", encoding="utf-8") as file:
                file.write(title + "\n" + article_body)
        except Exception as e:
            print(f"Failed to extract URL_ID {url_id}: {e}")

def perform_analysis(output_file):
    results = []
    for file in os.listdir("articles"):
        if file.endswith(".txt"):
            url_id = file.split(".")[0]
            with open(f"articles/{file}", "r", encoding="utf-8") as f:
                text = f.read()
            analysis = analyze_text(text)
            analysis["URL_ID"] = url_id
            results.append(analysis)

    output_df = pd.DataFrame(results)
    output_df.to_excel(output_file, index=False)


if __name__ == "__main__":
input_file = "Input.xlsx"
output_file = "Output Data Structure.xlsx"

print("Extracting articles...")
extract_articles(input_file)

print("Performing text analysis...")
perform_analysis(output_file)

print(f"Text analysis completed. Results saved in {output_file}.")