import os
import pandas as pd
from article_extraction import extract_articles
from text_analysis import TextAnalyzer
from stopwords_loader import load_stopwords, load_word_list

def main():
    input_file = "input/Input.xlsx"
    articles_folder = "articles"
    output_file = "output/Output.xlsx"
    

    stopwords = load_stopwords("StopWords")
    positive_words = load_word_list("MasterDictionary//positive-words.txt")
    negative_words = load_word_list("MasterDictionary//negative-words.txt")
    

    print("Extracting articles...")
    extract_articles(input_file, articles_folder)
    

    print("Performing text analysis...")
    analyzer = TextAnalyzer(stopwords, positive_words, negative_words)
    results = []

    for file_name in os.listdir(articles_folder):
        file_path = os.path.join(articles_folder, file_name)
        url_id = file_name.replace(".txt", "")
        analysis = analyzer.analyze(file_path)
        analysis["URL_ID"] = url_id
        results.append(analysis)


    output_df = pd.DataFrame(results)
    output_df.to_excel(output_file, index=False)
    print(f"Analysis results saved to {output_file}")

if __name__ == "__main__":
    main()
