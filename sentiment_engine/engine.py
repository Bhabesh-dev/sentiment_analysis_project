from transformers import pipeline

class SentimentAnalysisEngine:
    def __init__(self):
        # Load pre-trained sentiment analysis model
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        # Load pre-trained text classification model
        self.classifier = pipeline("zero-shot-classification")
        # Predefined categories
        self.categories = ["shopping", "investment", "entertainment", "technology"]

    def analyze(self, text):
        # Analyze sentiment
        sentiment_result = self.sentiment_analyzer(text)[0]
        sentiment_score = sentiment_result['score'] if sentiment_result['label'] == 'POSITIVE' else -sentiment_result['score']

        # Classify text into one of the predefined categories
        category_result = self.classifier(text, candidate_labels=self.categories)
        category = category_result['labels'][0]

        return sentiment_score, category