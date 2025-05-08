from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a helpful assistant for developers. Assist with coding, fixing bugs, and generating code.

Conversation history:
{context}

User question:
{question}

Assistant:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(context: str, question: str) -> str:
    response = chain.invoke({"context": context, "question": question})
    return response