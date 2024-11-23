def remove_punctuation(text):
    import string
    text = ''.join([char for char in text if char not in string.punctuation])

    return text

def tokenize(text):
    tokens = text.lower().split()
    return tokens


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
def remove_stopwords(text):

    text = [word for word in text if word not in stop_words]
    return text


from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def vectorize_column(df, column_name, max_ft):
    vectorizer = TfidfVectorizer(max_features =max_ft)
    vectors = vectorizer.fit_transform(df[column_name])
    
    return pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names_out())

def list_to_string(lst):
    return ' '.join(lst)

prefix = "summarize: "
def preprocess_function(examples, tokenizer):

    inputs = [prefix + doc for doc in examples["text"]]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True)

    labels = tokenizer(text_target=examples["summary"], max_length=128, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs