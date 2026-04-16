# Mental Health Classifier App

## Project Overview
This project is a deployment version of the NLP Mental Health Classifier. It provides a working system where a trained machine learning model is integrated with an API and a Streamlit user interface to predict mental health categories from text input.

The project demonstrates how a trained NLP model can be converted into a usable application using FastAPI and Streamlit, making it accessible for real-world interaction.

---

## Features
- Trained NLP model for mental health text classification
- REST API built using FastAPI
- Interactive Streamlit web application
- Real-time predictions from user input text
- Modular structure separating model, API, and UI

---

## Project Structure
```text
Mental-Health-Classifier-App/
│
├── model/
│   ├── model.pkl          # Trained ML model
│   └── vectorizer.pkl     # NLP Vectorizer
│
├── api/
│   └── MentalHealth.py    # FastAPI backend
│
├── app/
│   └── app.py             # Streamlit frontend
│
├── requirements.txt       # Project dependencies
└── README.md
```

---

## Setup Instructions

1. Install dependencies:
pip install -r requirements.txt

2. Download spaCy model:
python -m spacy download en_core_web_sm

3. Run API:
uvicorn MentalHealth:app --reload

4. Run Streamlit UI:
streamlit run app.py

---

## How It Works
1. User enters text into the Streamlit interface  
2. Input is sent to the FastAPI backend  
3. The model processes the text using the trained vectorizer  
4. The predicted mental health category is returned and displayed  

---

## Tech Stack
- Python  
- Scikit-learn  
- FastAPI  
- Streamlit  
- SpaCy  
- Pandas & NumPy  

---

## Related Project
Training Phase Repository: [NLP-Mental-Health-Classifier  ](https://github.com/ammarbinyasser01/NLP-Mental-Health-Classifier)

---

## Purpose of This Project
This project demonstrates the full lifecycle of an NLP system — from model training to deployment — showing how machine learning models can be turned into real-world applications with APIs and user interfaces.
