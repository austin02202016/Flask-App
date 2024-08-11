from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
import streamlit as st


# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# https://github.com/austin02202016/Flask-App.git
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    completion = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    message = completion.choices[0].message.content
    return message

# Streamlit interface
def main():
    st.title("Flask and Streamlit Integration")
    user_input = st.text_input("Enter your input:")
    
    if st.button("Get Response"):
        # Using Flask's test client to simulate a POST request
        with app.test_client() as client:
            response = client.post('/get_response', data={'user_input': user_input})
            st.write("Response:", response.get_data(as_text=True))

if __name__ == "__main__":
    main()  # Streamlit manages the server, so we don't need app.run()
