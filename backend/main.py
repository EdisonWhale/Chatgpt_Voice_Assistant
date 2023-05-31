# uvicorn main:app
# uvicorn main:app --reload
from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custiom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response


app = FastAPI()

# CORS -Origins
origins = [
    "http://localhost:5173"
    "http://localhost:5174"
    "http://localhost:4173"
    "http://localhost:4174"
    "http://localhost:3000"
]

# CORS -Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Check Health


@app.get("/health")
async def check_health():
    return {"message": "healthy"}


@app.get("/post-audio-get/")
async def get_audio():

    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)
    print(message_decoded)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    # Get Chatgpt Response
    chat_response = get_chat_response(message_decoded)

    print(chat_response)

    return "Done"

# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio")
# async def post_audio(file:UploadFile = File(...)):
#    print("hello")
