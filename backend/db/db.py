from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client.chatdb
collection = db.sessions

async def create_session(session_id: str):
    await collection.insert_one({
        "session_id": session_id,
        "conversation": "",
        "status": "active"
    })

async def update_session_status(session_id: str, status: str):
    await collection.update_one(
        {"session_id": session_id},
        {"$set": {"status": status}}
    )

async def save_conversation(session_id: str, conversation: str):
    await collection.update_one(
        {"session_id": session_id},
        {"$set": {"conversation": conversation}}
    )
