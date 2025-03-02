import unittest
from app import analyze_text

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentences(self):
        self.assertEqual(analyze_text("I love programming"), "Positive 😀")
        self.assertEqual(analyze_text("This is amazing!"), "Positive 😀")
        self.assertEqual(analyze_text("What a wonderful day!"), "Positive 😀")
        self.assertEqual(analyze_text("I feel great and excited"), "Positive 😀")
        self.assertEqual(analyze_text("Life is beautiful"), "Positive 😀")
        self.assertEqual(analyze_text("The movie was fantastic"), "Positive 😀")

    def test_negative_sentences(self):
        self.assertEqual(analyze_text("I absolutely hate waking up early"), "Negative 😞")
        self.assertEqual(analyze_text("This is the worst day of my miserable life"), "Negative 😞")
        self.assertEqual(analyze_text("I am extremely disappointed and heartbroken"), "Negative 😞")
        self.assertEqual(analyze_text("Nothing ever goes right for me, everything is a disaster"), "Negative 😞")
        self.assertEqual(analyze_text("I'm feeling very lonely and depressed"), "Negative 😞")
        self.assertEqual(analyze_text("Everything is falling apart, and I can't handle it"), "Negative 😞")

    def test_neutral_sentences(self):
        self.assertEqual(analyze_text("I went to the store today"), "Neutral 😐")
        self.assertEqual(analyze_text("It is what it is"), "Neutral 😐")
        self.assertEqual(analyze_text("The book is on the table"), "Neutral 😐")
        self.assertEqual(analyze_text("I saw a bird in the sky"), "Neutral 😐")
        self.assertEqual(analyze_text("Water is essential for life"), "Neutral 😐")
        self.assertEqual(analyze_text("I have a meeting at 3 PM"), "Neutral 😐")

if __name__ == '__main__':
    unittest.main()