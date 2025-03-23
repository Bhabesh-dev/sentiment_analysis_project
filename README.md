# Sentiment Analysis Project

This project consists of two modules:
1. **Sentiment Analysis Engine (API)**: A FastAPI server that performs sentiment analysis and text classification.
2. **Sentiment Analysis UI**: A Streamlit application that interacts with the API.

---

## **Folder Structure**
sentiment_analysis_project/
│
├── sentiment_engine/ # Sentiment Analysis Engine (API)
│ ├── init.py # Makes sentiment_engine a package
│ ├── engine.py # Core sentiment analysis logic
│ ├── api.py # FastAPI endpoint
│ ├── requirements.txt # Dependencies for the API
│ └── tests/ # Unit tests for the engine
│ ├── init.py
│ └── test_engine.py
│
├── sentiment_ui/ # Streamlit UI (Separate module)
│ ├── app.py # Streamlit application
│ └── requirements.txt # Dependencies for the UI
│
├── README.md # Overall project README
└── run.py # Entry point to run the API



---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/sentiment-analysis-project.git
cd sentiment-analysis-project

## **Using the Streamlit UI**

1. Open the Streamlit UI in your browser (`http://localhost:8501`).
2. Enter text in the text area:
   - Example: `"I love this new phone! It's amazing."`
3. Click the **Analyze** button.
4. View the results:
   - **Sentiment Score**: A number between -1 and 1.
   - **Category**: One of the predefined categories (`shopping`, `investment`, `entertainment`, `technology`).

---

## **Example Output**

### **Input**
- Text: `"I love this new phone! It's amazing."`

### **Output**