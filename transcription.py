import whisper  #in console: pip install openai-whisper

def transcripcion(archivo_mp3):
    model = whisper.load_model("base")  #also large
    result = model.transcribe(archivo_mp3)
    transcription_text = result["text"]
    with open("transcription_name.txt", "w") as file:
        file.write(transcription_text)
    return f"Transcripción guardada"

file_mp3 = "audio.mp3" #path or audio name, e.g., '/path/to/download/folder'

transcripcion(file_mp3)
