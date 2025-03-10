# Sentiment Analysis Web App

## Overview
This is a simple sentiment analysis web application built using Flask and VADER Sentiment Analysis. The application allows users to input text and receive a sentiment classification as **Positive 😀**, **Negative 😞**, or **Neutral 😐** based on the compound sentiment score from VADER.

## Features
- Built with **Flask** to create a lightweight web application.
- Uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** for sentiment analysis.
- Classifies text into three categories: **Positive**, **Negative**, or **Neutral**.
- Implements **unit testing** using `unittest` to validate accuracy.
- Achieves a **Pylint score of 10**, indicating well-structured and clean code.

## Installation

### Prerequisites
Ensure you have Python installed on your system (Python 3 recommended). Install the required dependencies using:

```bash
pip install flask vaderSentiment
```

## Usage
1. Run the Flask application:

```bash
python app.py
```

2. Open a web browser and go to:
```
http://127.0.0.1:5000/
```

3. Enter a sentence in the text box and click **Submit** to see the sentiment analysis result.

## Project Structure
```
📁 SentimentAnalysisApp
│── app.py              # Main Flask application
│── templates/
│   └── index.html      # Frontend template
│── unit-test.py            # Unit test cases for sentiment analysis
│── README.md           # Project documentation
```

## Code Explanation
- **`app.py`**:
  - Imports Flask and VADER Sentiment Analysis.
  - Defines the `analyze_text()` function that calculates sentiment scores.
  - Implements the Flask route (`/`) to handle user input and display results.
  
- **Sentiment Analysis Logic**:
  - If the **compound score** from VADER is **≥ 0.05**, the sentiment is **Positive 😀**.
  - If the **compound score** is **≤ -0.05**, the sentiment is **Negative 😞**.
  - Otherwise, the sentiment is classified as **Neutral 😐**.

- **`tests.py`**:
  - Contains **unit tests** to validate sentiment classifications.
  - Tests a variety of positive, negative, and neutral statements.

## Running Tests
To run the unit tests and validate sentiment analysis:

```bash
python -m unittest tests.py
```

If all tests pass, you will see:
```
----------------------------------------------------------------------
Ran 3 tests in 0.01s

OK
```

## Author
Rajat Rajput

## License
This project is licensed under the MIT License.

