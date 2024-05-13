import nltk
import string
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer


nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')


def get_wordnet_pos(pos_tag):
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