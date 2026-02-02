# 10X AI Internship Assignment – Task 1  
**Open-Source AI Model Deployment (Text & Speech)**

---

## Project Overview
This repository contains the implementation of **Task 1** of the **10X AI Internship Assignment**.  
The objective of this task is to demonstrate the ability to **deploy, run, and interact with open-source AI models**, focusing on **text processing** and **speech processing**.

The implementation is intentionally kept **simple, clear, and reproducible**, prioritizing system understanding and deployment clarity over UI complexity.

---

##  Task Objective
- Deploy one **open-source text-to-text language model**
- Deploy one **open-source speech-based AI model**
- Demonstrate basic **input → output** interaction
- Explain **model selection** and **deployment approach**

---

##  Models Used

### 1️⃣ Text-to-Text Language Model
- **Model Name:** FLAN-T5 Small  
- **Type:** Open-source text-to-text language model  
- **Framework:** HuggingFace Transformers  
- **Input:** Text prompt  
- **Output:** Generated text response  
- **Deployment:** Local execution using Python (CPU)

**Reason for Selection:**  
FLAN-T5 Small is lightweight, open-source, and suitable for running on systems without GPU, making it ideal for demonstrating basic text generation functionality.

---

### 2️ Speech-Based AI Model
- **Model Name:** Whisper  
- **Type:** Open-source speech recognition model  
- **Input:** Audio file (.wav / .m4a)  
- **Output:** Transcribed text  
- **Deployment:** Local execution using Python (CPU)

**Reason for Selection:**  
Whisper provides accurate speech-to-text conversion and supports multiple audio formats, making it a reliable choice for speech-based AI demonstrations.

---

##  Input & Output Demonstration

### Text Model
- **Input:** User-provided text prompt  
- **Output:** AI-generated textual response  

### Speech Model
- **Input:** Audio file containing spoken speech  
- **Output:** Converted text transcription  

> Note: Any valid audio file can be used as input to test the speech model.

---

## ⚙️ Setup & Execution

### Install Required Dependencies
```bash
pip install transformers torch sentencepiece openai-whisper ffmpeg-python
---

##  Task 2: Speech-to-Speech AI Assistant (LUCA)

###  Overview
Task 2 focuses on building a simple **speech-to-speech AI assistant** named **LUCA**.  
The objective of this task is to demonstrate the complete AI interaction loop:
- Voice input
- Speech recognition
- Language understanding
- Voice-based response

---

###  Model & Tools Used
- **Speech-to-Text:** OpenAI Whisper
- **Text Generation:** Google FLAN-T5 (small)
- **Text-to-Speech:** pyttsx3
- **Programming Language:** Python 3.10

---

### File
- `luca_assistant.py` – Implements the LUCA voice assistant

---

###  How LUCA Works
1. Records user voice input through microphone  
2. Converts speech to text using Whisper  
3. Generates a response using a language model  
4. Converts the response back to speech using TTS  

---

###  Speech Recognition Optimization (IMPORTANT)

**Speech recognition accuracy was improved by enforcing language constraints and reducing model randomness using Whisper configuration parameters.**

The following optimizations were applied:
- Forced English language detection (`language="en"`)
- Reduced randomness using `temperature=0.0`
- Disabled contextual hallucinations using `condition_on_previous_text=False`
- Used FP32 inference for CPU compatibility

These improvements helped reduce transcription ambiguity for short spoken commands and increased response reliability.

---

###  How to Run Task 2

```bash
py -3.10 luca_assistant.py

