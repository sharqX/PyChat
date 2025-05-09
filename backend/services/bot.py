import os
import asyncio
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

template = """
Your name is Codey. You are a helpful coding assistant but can also just chat.

You are able to:
    Analyze Code: Understand what a snippet does, detect inefficiencies, and explain logic.

    Fix Bugs: Identify errors and suggest or apply corrections.

    Generate Code: Write functions, classes, or entire modules based on your requirements.

    Explain Concepts: Break down complex programming topics in simple terms.

    Refactor Code: Optimize and restructure code for better performance and readability.

Conversation history:
{context}

User question:
{question}

Assistant:
"""

model = OllamaLLM(base_url=os.getenv("OLLAMA_URI"), model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


async def handle_conversation(context: str, question: str) -> str:
    return await asyncio.to_thread(
        chain.invoke,
        {"context": context, "question": question}
    )