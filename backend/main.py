from fastapi.middleware.cors import CORSMiddleware
from api.routes import *
import ollama
import httpx
import time
import os

app.add_middleware(
    CORSMiddleware,
    allow_origins=["ws://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def check_ollama(client: ollama.Client):
    tries = 5
    while True:
        try:
            client.ps()
            break
        except httpx.HTTPError:
            if tries:
                tries -= 1
                time.sleep(1)
            else:
                raise            

def check_model(client: ollama.Client, model: str):
    existing_models = client.list()
    models = [model.model for model in existing_models.models]
    if model not in models:
        print(f"Model not found, downloading: {model}")
        client.pull(model)
    else:
        print(f"Model found: {model}")

client = ollama.Client(host=os.getenv("OLLAMA_URI"))
check_ollama(client)
check_model(client, os.getenv("MODEL"))
    