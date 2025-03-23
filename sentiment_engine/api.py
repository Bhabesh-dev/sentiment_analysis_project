from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from .engine import SentimentAnalysisEngine

app = FastAPI()
engine = SentimentAnalysisEngine()

# Define a Pydantic model for the request body
class AnalyzeRequest(BaseModel):
    text: str

class FeedbackRequest(BaseModel):
    text: str
    correct_category: str

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    """
    Analyze the sentiment and category of the provided text.
    - **text**: The input text to analyze.
    """
    sentiment_score, category = engine.analyze(request.text)
    return {"sentiment_score": sentiment_score, "category": category}

@app.post("/feedback")
async def feedback(request: FeedbackRequest):
    """
    Provide feedback to improve the model.
    - **text**: The input text.
    - **correct_category**: The correct category for the text.
    """
    engine.add_feedback(request.text, request.correct_category)
    return {"message": "Feedback received."}

@app.post("/fine-tune")
async def fine_tune():
    """
    Fine-tune the model using the feedback data.
    """
    engine.fine_tune()
    return {"message": "Model fine-tuned."}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Analyze the sentiment and category of the content of an uploaded file.
    - **file**: A text file to analyze.
    """
    content = await file.read()
    text = content.decode("utf-8")
    sentiment_score, category = engine.analyze(text)
    return {"filename": file.filename, "sentiment_score": sentiment_score, "category": category}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)