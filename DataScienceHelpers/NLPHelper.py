import nltk
import pandas as pd
import string

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('wordnet')


def get_wordnet_pos(pos_tag):
    """Get part of speech.

    Args:
        pos_tag (str): Speech tag.

    Returns:
        number: Sense number.
    """
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def clean_text(text):
    """Clean-up and lemmatize text. Clean-up contains lower-casing, removing punctuation, 
    removing stop-words, removeing empty tokens and words consisting of one letter.

    Args:
        text (str): Text to be cleaned-up and lemmatized.

    Returns:
        str: Cleaned-up and lemmatized text.
    """
    # Convert to lower case
    text = text.lower()
    # Split to words and remove punctuation
    text = [word.strip(string.punctuation) for word in text.split(' ')]
    # Remove digits from the text
    text = [word for word in text if not any(c.isdigit() for c in word)]
    # Remove stop words
    stop = stopwords.words('english')
    text = [word for word in text if word not in stop]
    # Remove empty tokens
    text = [word for word in text if len(word) > 0]
    # Pos tag text
    pos_tags = pos_tag(text)
    # Lemmatize the text
    text = [WordNetLemmatizer().lemmatize(t[0], get_wordnet_pos(t[1])) for t in pos_tags]
    # Remove words consisting of one letter
    text = [word for word in text if len(word) > 1]
    # Join the text
    text = ' '.join(text)
    return (text)


def analyze_tonality(text):
    """Analize text tonality.

    Args:
        text (str): Text for which tonality must be analyzed.

    Returns:
        tuple: Polarity scores.
    """
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)


def vectorize_texts(texts):
    """Vectorize texts passed as a series. Usage:
        doc2vec_df = vectorize_texts(df['col'])
        df = pd.concat([df, doc2vec_df], axis=1)

    Args:
        texts (Series): Text values to be vectorized.

    Returns:
        DataFrame: DataFrame consisting of columns representing vectorized text.
    """
            
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(texts.apply(lambda x: x.split(' ')))]
    model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
    doc2vec_df = texts.apply(lambda x: model.infer_vector(x.split(' '))).apply(pd.Series)
    doc2vec_df.columns = ['doc2vec_vector_' + str(x) for x in doc2vec_df.columns]
    return doc2vec_df


def get_tf_idfs(texts, indexes):
    """Get estimates of word importance in the text.
        tfidf_df = get_tf_idfs(df['col'], df.index)
        df = pd.concat([df, tfidf_df], axis=1)

    Args:
        texts (Series): Text values to be analyzed.
        indexes (Series): DataFrame index.

    Returns:
        DataFrame: DataFrame consisting of columns representing importance of single words.
    """
    
    tfidf = TfidfVectorizer(min_df = 10)
    tfidf_result = tfidf.fit_transform(texts).toarray()
    tfidf_df = pd.DataFrame(tfidf_result, columns = tfidf.get_feature_names())
    tfidf_df.columns = ["word_" + str(x) for x in tfidf_df.columns]
    tfidf_df.index = indexes
    return tfidf_df