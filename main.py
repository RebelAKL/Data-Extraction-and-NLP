import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
import re


from article_extraction import extract_articles
from text_analysis import analyze_text
import pandas as pd

if __name__ == "__main__":
  input_file = "Input.xlsx"
  output_file = "Output Data Structure.xlsx"

  print("Extracting articles...")
  extract_articles(input_file)

  print("Performing text analysis...")
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

  print(f"Text analysis completed. Results saved in {output_file}.")