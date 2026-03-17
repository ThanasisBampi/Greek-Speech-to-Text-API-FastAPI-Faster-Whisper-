from fastapi import FastAPI
from pydantic import BaseModel
import base64
import os

from fast_whisper import fast_whisper_transcribe

app = FastAPI()

UPLOAD_FOLDER = #<path>
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class AudioData(BaseModel):
    filename: str
    audio_base64: str


@app.post("/upload-audio/")
async def upload_audio(data: AudioData):
    try:
        # 1️⃣ Decode Base64
        audio_bytes = base64.b64decode(data.audio_base64)

        # 2️⃣ Create full save path using original filename
        filename = os.path.basename(data.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)

        # 3️⃣ Save file directly 
        with open(save_path, "wb") as f:
            f.write(audio_bytes)

        # 4️⃣ Transcribe using Fast Whisper
        text, info = fast_whisper_transcribe(save_path)

        # 5️⃣ Clean up saved file
        os.remove(save_path)

        return {
            "message": "Audio saved successfully",
            "saved_as": data.filename,
            "transcription": text
        }
    
        

    except Exception as e:
        return {"error": str(e)}
