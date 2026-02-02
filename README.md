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
