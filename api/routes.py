import uuid
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from schemas.user_input import UserInput
from services.bot import handle_conversation
from db.db import create_session, update_session ,end_session



router = APIRouter()

conversation_cache = {}  # in-memory conversation tracking
@router.post("/")
async def chat(request: Request, user_input: UserInput):
    session_id = request.headers.get("X-Session-ID")

    # If no session_id → new session
    if not session_id:
        session_id = str(uuid.uuid4())
        await create_session(session_id)
        conversation_cache[session_id] = ""
        new_session = True
    else:
        if session_id not in conversation_cache:
            return JSONResponse(
                status_code=400,
                content={"detail": "Invalid session_id. Start a new session."}
            )
        new_session = False

    context = conversation_cache.get(session_id, "")

    if user_input.message.lower() in {"bye", "exit"}:
        await end_session(session_id, context)
        conversation_cache.pop(session_id, None)
        return JSONResponse(
            content={"response": "Session ended. Goodbye!", "session_id": session_id}
        )

    response = handle_conversation(context, user_input.message)
    updated_context = context + f"\nUser: {user_input.message}\nAI: {response}"
    conversation_cache[session_id] = updated_context
    await update_session(session_id, updated_context)

    return JSONResponse(
        content={"response": response, "session_id": session_id}
    )