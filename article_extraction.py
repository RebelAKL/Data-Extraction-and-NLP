import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_articles(input_file):
  df = pd.read_excel(input_file)
  os.makedirs("articles", exist_ok=True)

  for index, row in df.iterrows():
    url_id = row["URL_ID"]
    url = row["URL"]

    if os.path.exists(f"articles/{url_id}.txt"):
      print(f"Article {url_id} already extracted.")
      continue
    
    try:
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')
      title = soup.find('h1').get_text(strip=True)
      article_body = soup.find('article').get_text(strip=True)
      
      with open(f"articles/{url_id}.txt", "w", encoding="utf-8") as file:
        file.write(title + "\n" + article_body)
    except Exception as e:
      print(f"Failed to extract URL_ID {url_id}: {e}")