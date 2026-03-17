from faster_whisper import WhisperModel


audio_file_path = #path

def fast_whisper_transcribe(audio_file_path):
    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"  # very fast on CPU
    )

    segments, info = model.transcribe(
        f"{audio_file_path}",                   
        language="el"
    )
    for segment in segments:
        text = segment.text
       
    return text, info

text, info = fast_whisper_transcribe(audio_file_path)
print(text)