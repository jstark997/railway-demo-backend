from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# Configure CORS - in production, replace "*" with your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your Railway frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Railway!"}

@app.get("/api/status")
def get_status():
    return {
        "status": "running",
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development")
    }

@app.post("/api/echo")
def echo_message(message: Message):
    return {
        "received": message.text,
        "length": len(message.text)
    }

@app.get("/api/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Item One", "description": "First demo item"},
            {"id": 2, "name": "Item Two", "description": "Second demo item"},
            {"id": 3, "name": "Item Three", "description": "Third demo item"}
        ]
    }
