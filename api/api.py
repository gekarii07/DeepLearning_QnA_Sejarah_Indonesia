from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import torch
from transformers import BertTokenizer, BertForQuestionAnswering
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inisialisasi FastAPI
app = FastAPI(title="API QnA Sejarah Indonesia")

# Load model dan tokenizer dari Hugging Face
model_repo = "gekkarii07/qna-sejarah-indonesia-bert-multilingual"
try:
    tokenizer = BertTokenizer.from_pretrained(model_repo)
    model = BertForQuestionAnswering.from_pretrained(model_repo)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Model gagal di-load dari Hugging Face: {e}")

# Load dataset untuk similarity
data_file = "data-deep-learning.csv"  
try:
    data = pd.read_csv(data_file)
    questions = data['question'].tolist()
    contexts = data['context'].tolist()
except Exception as e:
    raise FileNotFoundError(f"Dataset tidak ditemukan: {e}")

# Preprocess dataset untuk TF-IDF
vectorizer = TfidfVectorizer()
context_vectors = vectorizer.fit_transform(contexts)

# Pydantic Model untuk Input
class QuestionInput(BaseModel):
    question: str

# Helper function untuk similarity matching
def find_most_similar_context(input_question: str):
    input_vector = vectorizer.transform([input_question])
    similarity_scores = cosine_similarity(input_vector, context_vectors).flatten()
    max_index = similarity_scores.argmax()
    similarity_percentage = similarity_scores[max_index] * 100
    return contexts[max_index], similarity_percentage

# Helper function untuk prediksi jawaban
def get_predicted_answer(question: str, context: str) -> str:
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    start_scores, end_scores = outputs.start_logits, outputs.end_logits

    start_idx = torch.argmax(start_scores)
    end_idx = torch.argmax(end_scores)

    answer_tokens = input_ids[0][start_idx:end_idx + 1]
    predicted_answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)
    return predicted_answer

# Endpoint untuk prediksi jawaban
@app.post("/predict")
async def predict(input_data: QuestionInput):
    try:
        # Cari context yang paling mirip
        matched_context, similarity_percentage = find_most_similar_context(input_data.question)

        # Prediksi jawaban
        predicted_answer = get_predicted_answer(input_data.question, matched_context)

        return {
            "input_question": input_data.question,
            "matched_context": matched_context,
            "similarity_score": f"{similarity_percentage:.2f}%",
            "predicted_answer": predicted_answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint untuk cek API
@app.get("/")
def read_root():
    return {"message": "API is running!"}