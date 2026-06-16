 # NLP Regex Toolkit

A web-based Natural Language Processing (NLP) and Regular Expression Toolkit built using Python and Flask. This project provides various text processing utilities such as information extraction, tokenization, text cleaning, validation, and custom regex matching through an interactive web interface.

##  Features

###  Information Extraction
Extract useful information from text using Regular Expressions:

- Email Addresses
- Phone Numbers
- Dates
- URLs
- Hashtags
- Social Media Mentions

###  Tokenization
Supports multiple tokenization methods:

- Word Tokenization
- Sentence Tokenization
- Alphabetic Tokenization
- NLTK-style Tokenization

###  Text Cleaning
Clean and preprocess text by:

- Removing URLs
- Removing HTML Entities
- Removing Emojis
- Removing Hashtags and Mentions
- Removing Special Characters
- Normalizing Extra Spaces

###  Data Validation
Validate common user inputs:

- Email Address
- Mobile Number
- Date
- PAN Card Number
- PIN Code
- URL

###  Custom Regex Matching
Test and execute custom regular expressions with support for:

- Global Matching
- Case-Insensitive Matching
- Multiline Matching

---

##  Tech Stack

- Python 3
- Flask
- Regular Expressions (Regex)
- HTML
- CSS
- JavaScript

---

##  Project Structure

```text
NLP/
│
├── app.py
├── regex_nlp.py
├── requirements.txt
├── LICENSE
├── README.md
│
└── templates/
    └── index.html
```

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/AT4455/NLP.git
cd NLP
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| /extract | POST | Extract emails, phones, dates, URLs, hashtags, and mentions |
| /tokenize | POST | Tokenize text using selected mode |
| /clean | POST | Clean and preprocess text |
| /validate | POST | Validate user input |
| /custom | POST | Perform custom regex matching |

---

##  Use Cases

- NLP Learning Projects
- Regex Pattern Testing
- Text Analytics
- Information Extraction
- Data Validation Systems
- Social Media Text Processing

---

##  Future Enhancements

- Named Entity Recognition (NER)
- Sentiment Analysis
- Language Detection
- PDF Text Extraction
- CSV Processing
- Advanced NLP Models

---

##  Author

**Thanuj Guptha**

GitHub: https://github.com/AT4455

---

##  License

This project is licensed under the MIT License.

If you found this project useful, consider giving it a star on GitHub!
