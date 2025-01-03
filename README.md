## **Text Analysis and Sentiment Analysis Project**

### **Overview**

This project is designed to perform text analysis and sentiment analysis on a collection of articles extracted from URLs. It calculates various metrics, such as sentiment scores, readability indices, and linguistic features, and outputs the results in a structured Excel file. The project involves two main tasks:

1. **Data Extraction**: Extracting textual content from the provided URLs.
2. **Text Analysis**: Performing in-depth linguistic and readability analysis on the extracted text.

---

### **Objective**

1. Extract article text from the provided URLs in `Input.xlsx` and save each article in a separate text file using the `URL_ID` as the filename.
2. Analyze the text to compute the following metrics:
   - Positive and Negative Sentiment Scores
   - Polarity and Subjectivity Scores
   - Readability indices like Fog Index
   - Word-level metrics such as Word Count, Syllable Count, Personal Pronouns, and Average Word Length
3. Save the results in `Output.xlsx` with the exact structure provided.

---

### **Why Spacy and BERT?**

Initially, **NLTK** was considered for tokenization and stopword removal. However, tokenization with NLTK raised Lookup error even after multiple diagnosis. Then the following libraries were considered :
- **Spacy**: A modern NLP library used for tokenization, stopword removal, and linguistic processing.
- **BERT**: Leveraged for advanced sentiment analysis to handle nuanced text better.

---

### **Folder Structure**

```
project/
│
├── input/
│   ├── Input.xlsx              # Input file with URLs and URL_IDs
│
├── StopWords/              # Folder containing multiple stopword files
│   ├── StopWords_Auditor.txt
│   ├── StopWords_Currencies.txt
│   ├── StopWords_DatesandNumbers.txt
│   ├── StopWords_Generic.txt
│   ├── StopWords_GenericLong.txt
│   ├── StopWords_Geographic.txt 
│   ├── StopWords_Names.txt
│
├── MasterDictionary/
│   ├── positive-words.txt      # Positive words dictionary
│   ├── negative-words.txt      # Negative words dictionary
│
├── articles/                   # Extracted articles will be saved here
│
├── output/
│   ├── Output.xlsx             # Final output file with analysis results
│
├── article_extraction.py       # Handles article extraction from URLs
├── text_analysis.py            # Performs text analysis and computes metrics
├── stopwords_loader.py         # Loads stopwords and dictionaries
├── main.py                     # Orchestrates the entire workflow
│
├── requirements.txt            # Required Python libraries
└── README.md                   # Project documentation
```

---

### **Installation and Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/RebelAKL/Data-Extraction-and-NLP.git
   cd Data-Extraction-and-NLP
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the input file (`Input.xlsx`) in the `input/` folder.

---

### **Execution**

1. Run the main script:
   ```bash
   python main.py
   ```

2. Output will be saved in the `output/Output.xlsx` file with the following columns:
   - `URL_ID`
   - `URL`
   - `POSITIVE SCORE`
   - `NEGATIVE SCORE`
   - `POLARITY SCORE`
   - `SUBJECTIVITY SCORE`
   - `AVG SENTENCE LENGTH`
   - `PERCENTAGE OF COMPLEX WORDS`
   - `FOG INDEX`
   - `AVG NUMBER OF WORDS PER SENTENCE`
   - `COMPLEX WORD COUNT`
   - `WORD COUNT`
   - `SYLLABLE PER WORD`
   - `PERSONAL PRONOUNS`
   - `AVG WORD LENGTH`

---

### **Key Features**

1. **Article Extraction**:
   - Extracts only the title and main content from the provided URLs.
   - Handles errors gracefully if a URL is inaccessible.

2. **Text Analysis**:
   - **Sentiment Scores**: Calculates positive, negative, polarity, and subjectivity scores.
   - **Readability Indices**: Computes metrics like Fog Index and Percentage of Complex Words.
   - **Linguistic Metrics**: Analyzes word count, syllable count, personal pronouns, and more.

3. **Stopword Management**:
   - Utilizes a comprehensive list of stopwords for cleaning text.
   - Includes stopword files for specific domains like currencies and geographic terms.

---

### **Improvements Over NLTK**

1. **Spacy**:
   - Faster and more accurate tokenization.
   - Built-in linguistic capabilities.
2. **BERT**:
   - Handles complex and nuanced sentiment analysis.
   - Suitable for financial and domain-specific text.

---

### **Dependencies**

The required libraries are listed in `requirements.txt`. Major dependencies include:
- `pandas`
- `beautifulsoup4`
- `requests`
- `spacy`
- `openpyxl`

---

