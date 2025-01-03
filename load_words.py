def load_word_list(file_path):
  with open(file_path, 'r', encoding='ISO-8859-1') as file:
    words = file.read().splitlines()
  return set(words)

positive_words = load_word_list("MasterDictionary\\positive-words.txt")
negative_words = load_word_list("MasterDictionary\\negative-words.txt")