from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a asistant of developer, help them with coding, fixing bugs and genrating code.

Here is the conversation history: {context}

Question {question}

Answer:
"""


model = OllamaLLM(model="codellama:13b")
promt = ChatPromptTemplate.from_template(template)
chain = promt | model

def handle_conversation(context: str, question: str) -> str:
    response = chain.invoke({"context": context, "question": question})
    return response