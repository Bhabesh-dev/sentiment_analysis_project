from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from .engine import SentimentAnalysisEngine

app = FastAPI()
engine = SentimentAnalysisEngine()

# Define a Pydantic model for the request body
class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    """
    Analyze the sentiment and category of the provided text.
    - **text**: The input text to analyze.
    """
    sentiment_score, category = engine.analyze(request.text)
    return {"sentiment_score": sentiment_score, "category": category}

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
    uvicorn