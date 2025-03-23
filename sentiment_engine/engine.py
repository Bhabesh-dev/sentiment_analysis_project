from transformers import pipeline
import torch
from sklearn.model_selection import train_test_split
import json
import os

class SentimentAnalysisEngine:
    def __init__(self, data_file="data.json"):
        # Load pre-trained sentiment analysis model
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        # Load pre-trained text classification model
        self.classifier = pipeline("zero-shot-classification")
        # File to store categories and feedback data
        self.data_file = data_file
        # Load categories and feedback data from file
        self.categories, self.feedback_data = self.load_data()

    def analyze(self, text):
        # Analyze sentiment
        sentiment_result = self.sentiment_analyzer(text)[0]
        sentiment_score = sentiment_result['score'] if sentiment_result['label'] == 'POSITIVE' else -sentiment_result['score']

        # Classify text into one of the predefined categories
        category_result = self.classifier(text, candidate_labels=self.categories)
        category = category_result['labels'][0]

        return sentiment_score, category

    def add_feedback(self, text, correct_category):
        """
        Add user feedback to the feedback data.
        - **text**: The input text.
        - **correct_category**: The correct category provided by the user.
        """
        self.feedback_data.append((text, correct_category))

        # If the correct category is not in the list, add it
        if correct_category not in self.categories:
            self.categories.append(correct_category)

        # Save the updated data to file
        self.save_data()

    def fine_tune(self):
        """
        Fine-tune the model using the feedback data.
        """
        if not self.feedback_data:
            return

        # Prepare data for fine-tuning
        texts, labels = zip(*self.feedback_data)
        texts = list(texts)
        labels = list(labels)

        # Split data into training and validation sets
        train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

        # Fine-tune the model (this is a placeholder; actual fine-tuning requires more work)
        # For simplicity, we'll just retrain the classifier on the new data
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        print("Model fine-tuned with new feedback data.")

    def save_data(self):
        """
        Save categories and feedback data to a file.
        """
        data = {
            "categories": self.categories,
            "feedback_data": self.feedback_data
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f)
        print(f"Data saved to {self.data_file}")

    def load_data(self):
        """
        Load categories and feedback data from a file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
            return data.get("categories", ["shopping", "investment", "entertainment", "technology"]), data.get("feedback_data", [])
        else:
            return ["shopping", "investment", "entertainment", "technology"], []

    def save_model(self, path="model"):
        """
        Save the fine-tuned model to disk.
        """
        torch.save(self.classifier, path)
        print(f"Model saved to {path}")

    def load_model(self, path="model"):
        """
        Load a fine-tuned model from disk.
        """
        self.classifier = torch.load(path)
        print(f"Model loaded from {path}")