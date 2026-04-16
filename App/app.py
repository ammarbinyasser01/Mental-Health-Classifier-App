import streamlit as st

# Streamlit UI
st.title("Mental Health Detection App")

user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
                # Replaces: result = predict_text(user_input)
        import requests
        
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"text": user_input}
        )
        
        result = response.json().get("prediction", "Error: No prediction found")
        st.success(f"Prediction: {result}")
