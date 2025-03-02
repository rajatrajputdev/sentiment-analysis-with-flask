"""
Import the Flask module to build a micro-website for implementing the sentiment analyzer.  
Import VADER Sentiment, a lexicon- and rule-based sentiment analysis tool.
"""

from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

def analyze_text(text):
    """
    Analyze the sentiment of the input text and return the result.
    """
    score = analyzer.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive 😀"
    if score["compound"] <= -0.05:
        return "Negative 😞"
    return "Neutral 😐"

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Implement the default Flask route to render the template, get user input, 
    and return the analyzed sentiment.
    """
    sentiment = None
    text = ""
    if request.method == "POST":
        sentiment = analyze_text(request.form["text"])
        text = request.form["text"]
    return render_template("index.html", sentiment=sentiment, text=text)


if __name__ == "__main__":
    app.run(debug=True)
