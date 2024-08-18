import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import base64

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Load pre-trained models and vectorizers
tf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Load stopwords once for efficiency
stop_words = set(stopwords.words('english'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    filtered_words = [i for i in text if i.isalnum()]
    filtered_words = [i for i in filtered_words if i not in stop_words and i not in string.punctuation]
    stemmed_words = [ps.stem(i) for i in filtered_words]
    return " ".join(stemmed_words)


# Function to convert local image to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Streamlit application
st.title("Email/SMS Spam Classifier")
input_sms = st.text_input("Enter the Message")

if st.button('Predict'):
    if input_sms:
        transformed_sms = transform_text(input_sms)
        vector_input = tf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        if result == 1:
            st.header("SPAM")
        else:
            st.header("NOT SPAM")
    else:
        st.warning("Please enter a message for classification.")
