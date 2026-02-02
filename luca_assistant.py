import whisper
from transformers import pipeline
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3

# -----------------------------
# 1. Record voice input
# -----------------------------
def record_audio(filename="input.wav", duration=5, fs=44100):
    print("🎤 Speak now (5 seconds)...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("✅ Audio recorded")

# -----------------------------
# 2. Speech to Text (ASR)
# -----------------------------
def speech_to_text(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(
        audio_file,
        language="en",        # Force English
        temperature=0.0,      # Stop guessing
        fp16=False,           # CPU safe
        condition_on_previous_text=False
    )
    return result["text"].strip()



# -----------------------------
# 3. Text AI + LUCA logic
# -----------------------------
def generate_response(user_text):
    llm = pipeline("text-generation", model="google/flan-t5-small")

    text = user_text.lower()

    # Robust LUCA identity detection
    if "who" in text and "you" in text:
        return "I am LUCA from 10X Technologies."

    if "your name" in text or "identify" in text:
        return "I am LUCA from 10X Technologies."

    response = llm(
        user_text,
        max_length=100,
        do_sample=False
    )
    return response[0]["generated_text"].strip()



# -----------------------------
# 4. Text to Speech (TTS)
# -----------------------------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    record_audio(duration=7)

    user_text = speech_to_text("input.wav")
    print("You said:", user_text)

    reply = generate_response(user_text)
    print("LUCA:", reply)

    speak(reply)

