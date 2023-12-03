"""from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the TfidfVectorizer used during training
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
   tfidf_vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        answer = request.form['answer']

        # Transform the input message using the pre-trained TfidfVectorizer
        input_features =  tfidf_vectorizer.transform([answer])

        # Make a prediction using the pre-trained model
        prediction = model.predict(input_features)

        # Convert the numeric prediction to a human-readable label
        result = 'Spam' if prediction[0] == 0 else 'Ham'

        return render_template('index.html', prediction_text=f'The message is a {result}')

if __name__ == '__main__':
    app.run(debug=True)"""
    
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the TfidfVectorizer used during training
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
   tfidf_vectorizer = pickle.load(vectorizer_file)

def main():
    st.title("Spam or Ham Prediction App")

    # Input text box for the user to enter the message
    answer = st.text_area("Enter your message here:")

    # Make a prediction when the user clicks the "Predict" button
    if st.button("Predict"):
        if not answer:
            st.warning("Please enter a message.")
        else:
            # Transform the input message using the pre-trained TfidfVectorizer
            input_features =  tfidf_vectorizer.transform([answer])

            # Make a prediction using the pre-trained model
            prediction = model.predict(input_features)

            # Convert the numeric prediction to a human-readable label
            result = 'Spam' if prediction[0] == 0 else 'Ham'

            # Display the prediction result
            st.success(f'The message is predicted to be: {result}')

if __name__ == '__main__':
    main()
    
