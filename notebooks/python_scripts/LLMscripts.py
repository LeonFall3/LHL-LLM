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

def vectorize_column(df, column_name):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(df[column_name])
    df[f"{column_name}_vectorized"] = list(vectors.toarray())
    
    return df

def list_to_string(list, sep=' '):
    return sep.join(list)
