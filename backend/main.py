# uvicorn main:app
# uvicorn main:app --reload
# .\venv\Scripts\activate

from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custiom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech
app = FastAPI()

# CORS -Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:8000",
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

# Reset Messages


@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # audio_input = open("voice.mp3", "rb")

    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)
    print(message_decoded)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    # Get Chatgpt Response
    chat_response = get_chat_response(message_decoded)

    # Guard: Ensure message decoded
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get response")

    # Store messages
    store_messages(message_decoded, chat_response)

    # Covert chat response to audio
    print(chat_response)
    audio_output = convert_text_to_speech(chat_response)

    # Guard: Ensure message decoded
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get ElevenLabs audio response")

    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
