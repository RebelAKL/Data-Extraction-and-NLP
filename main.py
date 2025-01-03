import os
import pandas as pd
from article_extraction import extract_articles
from text_analysis import TextAnalyzer
from stopwords_loader import load_stopwords, load_word_list

def main():
    input_file = "input/Input.xlsx"
    articles_folder = "articles"
    output_file = "output/Output.xlsx"
    

    stopwords = load_stopwords("dictionaries/StopWords")
    positive_words = load_word_list("dictionaries/positive-words.txt")
    negative_words = load_word_list("dictionaries/negative-words.txt")

    print("Extracting articles...")
    extract_articles(input_file, articles_folder)
    

    print("Performing text analysis...")
    analyzer = TextAnalyzer(stopwords, positive_words, negative_words)
    results = []

    input_df = pd.read_excel(input_file)

    for _, row in input_df.iterrows():
        url_id = row["URL_ID"]
        url = row["URL"]
        file_path = os.path.join(articles_folder, f"{url_id}.txt")

        if os.path.exists(file_path):
            analysis = analyzer.analyze(file_path)
            analysis["URL_ID"] = url_id
            analysis["URL"] = url
            results.append(analysis)
        else:
            print(f"File for URL_ID {url_id} not found. Skipping...")


    output_df = pd.DataFrame(results)


    column_order = [
        "URL_ID", "URL", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE",
        "SUBJECTIVITY SCORE", "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS",
        "FOG INDEX", "AVG NUMBER OF WORDS PER SENTENCE", "COMPLEX WORD COUNT",
        "WORD COUNT", "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"
    ]
    output_df = output_df[column_order]

    output_df.to_excel(output_file, index=False)
    print(f"Analysis results saved to {output_file}")

if __name__ == "__main__":
    main()
