import spacy
from positive_words import positive_words, negative_words

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