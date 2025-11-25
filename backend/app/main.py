from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

app = FastAPI(title="MyCask API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"message": "Welcome to the MyCask API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}