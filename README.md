🎙️ Greek Speech-to-Text API
---------------------------
    FastAPI + Faster Whisper
    A lightweight speech-to-text API built with FastAPI that transcribes Base64-encoded audio files into text using Faster Whisper.
    Optimized for Greek speech recognition (el) and fast CPU inference.


Features:
---------
    ⚡ FastAPI REST API
    🎧 Accepts Base64 audio uploads
    🧠 Transcription using Faster Whisper
    🇬🇷 Greek language support
    💾 Temporary file storage
    🧹 Auto-delete after processing
    ⚙️ CPU optimized (int8)


🧠 About Faster Whisper:
-------------------------
    This project uses Faster Whisper, a high-performance implementation of OpenAI’s Whisper model that is
    up to ~4x faster and more memory efficient thanks to CTranslate2 optimizations.


📦 Installation
-----------------
    # Clone the repository
        git clone https://github.com/ThanasisBampi/Greek-Speech-to-Text-API-FastAPI-Faster-Whisper-.git
        cd Greek-Speech-to-Text-API-FastAPI-Faster-Whisper-
    
    # Create virtual environment
        python -m venv venv
        source venv/bin/activate # Windows: venv\Scripts\activate
    
    # Install dependencies
        pip install fastapi uvicorn pydantic faster-whisper



▶️ Run the API
---------------
    uvicorn main:app --reload


Request
---------
    {
    "filename": "audio.mp3",
    "audio_base64": "BASE64_STRING"
    }


Response
---------
    {
    "message": "Audio saved successfully",
    "saved_as": "audio.mp3",
    "transcription": "Καλημέρα σας"
    }


How It Works:
---------------
    Client sends Base64 audio
    API decodes the audio
    File is saved temporarily
    Transcription runs via Faster Whisper
    Result is returned
    File is deleted


📁 Project Structure
---------------------
    .
    ├── main.py # FastAPI server
    ├── fast_whisper.py # Whisper transcription logic
    └── README.md


🔧 Configuration
---------------------
    update upload path in main.py:
    UPLOAD_FOLDER = "your/path/here"


🧪 Example Client:
----------------------
    import base64
    import requests
    
    url = "http://127.0.0.1:8000/upload-audio/"
    
    with open("audio.mp3", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode()
    
    response = requests.post(url, json={
    "filename": "audio.mp3",
    "audio_base64": audio_base64
    })
    
    print(response.json())

Author
Thanasis Bampi
