from flask import Flask, render_template
import requests

# Define API URL.
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

# Initialize Flask.
app = Flask(__name__)

# Define routing.
@app.route('/')
def index():
    # Make API Call - make sure to use a valid API key.
    api_key = 'uuD257ZE+lUjbacXp2i+Yw==GsuKaejkcfXsE3xt'
    resp = requests.get(TRIVIA_URL, headers={'X-Api-Key': api_key }).json()
    # Get first trivia result since the API returns a list of results.
    trivia = resp[0]
    # Render HTML using the trivia question and answer.
    return render_template('index.html', question=trivia['question'], answer=trivia['answer'])

if __name__ == '__main__':
    app.run(debug=True)  # Убедитесь, что сервер запускается
