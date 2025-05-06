from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from bot import handle_conversation
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str
    role: str = "human"

conversation_history = {}  # Store history by conversation_id

@app.post("/")
async def chat(user_input: UserInput):
    conv_id = str(uuid.uuid4())
    prev_context = conversation_history.get(conv_id, "")

    # Call LLM
    response = handle_conversation(prev_context, user_input.message)

    # Update history
    updated_context = f"{prev_context}\nUser: {user_input.message}\nAI: {response}"
    conversation_history[conv_id] = updated_context

    return {"response": response}
