from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import *

app.add_middleware(
    CORSMiddleware,
    allow_origins=["ws://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)