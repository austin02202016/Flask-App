from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

if __name__ == '__main__':
    app.run(debug=True)
