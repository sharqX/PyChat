from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from services.bot import handle_conversation
from db.db import create_session, update_session_status, save_conversation
import uuid

app = FastAPI()

@app.websocket("/")
async def chat(websocket: WebSocket):
    await websocket.accept()
    session_id = str(uuid.uuid4())
    context = ""

    await create_session(session_id)  # Insert with status: active
    await update_session_status(session_id, "active")

    try:
        while True:
            data = await websocket.receive_text()

            if data.lower() in {"bye", "exit"}:
                await websocket.send_text("Session ended. Goodbye!")
                await update_session_status(session_id, "closed")
                await save_conversation(session_id, context)
                await websocket.close()
                break

            response = await handle_conversation(context, data)
            context += f"\nUser: {data}\nAI: {response}"
            await websocket.send_text(response)

    except WebSocketDisconnect:
        await update_session_status(session_id, "closed")
        await save_conversation(session_id, context)