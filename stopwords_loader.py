import os

def load_stopwords(folder_path):

    stopwords = set()
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r", encoding="ISO-8859-1") as file:
            stopwords.update(file.read().splitlines())
    return stopwords

def load_word_list(file_path):

    with open(file_path, "r", encoding="ISO-8859-1") as file:
        return set(file.read().splitlines())
