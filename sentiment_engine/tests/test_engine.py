import unittest
from sentiment_engine.engine import SentimentAnalysisEngine

class TestSentimentAnalysisEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SentimentAnalysisEngine()

    def test_analyze(self):
        # Test sentiment analysis and classification
        text = "I love this new phone! It's amazing."
        sentiment_score, category = self.engine.analyze(text)

        # Assertions
        self.assertIsInstance(sentiment_score, float)
        self.assertIn(category, self.engine.categories)

if __name__ == "__main__":
    unittest.main()