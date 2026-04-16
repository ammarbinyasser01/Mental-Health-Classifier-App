from fastapi import FastAPI
from pydantic import BaseModel
import pickle, re
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load model and TF-IDF
model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

# NLP tools
nlp = spacy.load("en_core_web_sm", disable=["parser","ner"])
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Preprocessing
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and len(t)>1]
    doc = nlp(" ".join(tokens))
    tokens = [token.lemma_ for token in doc]
    return " ".join(tokens)

def predict_text(input_text):
    processed = preprocess_text(input_text)
    vector = tfidf.transform([processed])
    prediction = model.predict(vector)[0]
    return "Mental Distress" if prediction==1 else "Normal"

# FastAPI app
app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input_data: TextInput):
    result = predict_text(input_data.text)
    return {"prediction": result}