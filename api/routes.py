from fastapi import APIRouter
from schemas.user_input import UserInput
from services.bot import handle_conversation
import uuid

router = APIRouter()

conversation_history = {}  

@router.post("/")
async def chat(user_input: UserInput):
    conv_id = str(uuid.uuid4())
    prev_context = conversation_history.get(conv_id, "")

    # Call LLM
    response = handle_conversation(prev_context, user_input.message)

    # Update history
    updated_context = f"{prev_context}\nUser: {user_input.message}\nAI: {response}"
    conversation_history[conv_id] = updated_context

    return {"response": response}