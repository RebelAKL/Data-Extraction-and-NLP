import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def extract_articles(input_file, output_folder):

    df = pd.read_excel(input_file)
    os.makedirs(output_folder, exist_ok=True)

    for index, row in df.iterrows():
        url_id = row["URL_ID"]
        url = row["URL"]

        if os.path.exists(f"{output_folder}/{url_id}.txt"):
            print(f"Article {url_id} already extracted.")
            continue
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1').get_text(strip=True)
            article_body = soup.find('article').get_text(strip=True)
            
            with open(f"{output_folder}/{url_id}.txt", "w", encoding="utf-8") as file:
                file.write(title + "\n" + article_body)
                print(f"Article {url_id} extracted successfully.")
        except Exception as e:
            print(f"Failed to extract URL_ID {url_id}: {e}")
