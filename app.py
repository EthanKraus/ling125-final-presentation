from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    # Pass `polarity=None` on the initial load
    return render_template('index.html', text=None, polarity=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Keep polarity as a float for accuracy
    return render_template('index.html', text=text, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
