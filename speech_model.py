import whisper

# Load Whisper model
model = whisper.load_model("base")

# Transcribe M4A audio file
result = model.transcribe("sample.m4a")

print("Recognized Text:")
print(result["text"])
