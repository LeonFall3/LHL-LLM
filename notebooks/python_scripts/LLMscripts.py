
def remove_punctuation(text):
    import string
    text = ''.join([char for char in text if char not in string.punctuation])

    return text

import re
def remove_html(text):
    clean_text = re.sub('<.*?>', '', text)
    return clean_text 

def remove_urls(text):
    clean_text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return clean_text

def remove_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    cleaned_text = re.sub(email_pattern, '', text)
    return cleaned_text

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')


def remove_stopwords(text):

    text = [word for word in text if word not in stop_words]
    return text


