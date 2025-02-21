from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-trained pipelines
sentiment_pipeline = pipeline("sentiment-analysis")
summarization_pipeline = pipeline("summarization")
qa_pipeline = pipeline("question-answering")

# Define request body schemas
class TextInput(BaseModel):
    text: str

class SummarizeInput(BaseModel):
    text: str

class QAInput(BaseModel):
    question: str
    context: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis, Summarization, and QA API!"}

# API endpoint for sentiment prediction
@app.post("/predict")
def predict(input: TextInput):
    result = sentiment_pipeline(input.text)
    return {"text": input.text, "prediction": result}

# API endpoint for text summarization
@app.post("/summarize")
def summarize(input: SummarizeInput):
    try:
        summary = summarization_pipeline(input.text, max_length=130, min_length=30, do_sample=False)
        return {"text": input.text, "summary": summary[0]["summary_text"]}
    except Exception as e:
        return {"error": str(e)}

# API endpoint for Question Answering
@app.post("/qa")
def answer_question(input: QAInput):
    result = qa_pipeline({
        "question": input.question,
        "context": input.context
    })
    return {"question": input.question, "answer": result['answer']}
