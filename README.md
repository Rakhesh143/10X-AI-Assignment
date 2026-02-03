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


# Task 3 – School AI Assistant (Intelligent Document-Based RAG)

## Overview
This project implements a **School AI Assistant** using a **Retrieval-Augmented Generation (RAG)** approach.
The assistant answers questions **strictly using the provided school PDF document** and does not use
any external knowledge.

A key strength of this system is that **users do not need to ask fixed or exact questions**.
Even natural and indirect questions are correctly understood and answered **as long as the information
exists in the PDF**.

---

## Key Highlights (IMPORTANT)
- Users do **NOT** need to ask exact section names like:
  - “Exam Schedule”
  - “School Rules”

- The assistant can correctly answer **natural questions**, such as:
  - When is Unit Test 1?
  - What is the mathematics time period?
  - Annual tuition fee entha?
  - How many students are there?
  - Who has the highest marks?

If the information is present in the PDF, the assistant **will retrieve and return the correct answer**.

---

## Features
- Answers **any question whose information exists in the PDF**
- Supports:
  - School rules
  - Fee structure (annual tuition fee, exam fee, transport fee)
  - Exam schedule (Unit Tests, Mid-Terms, Final Exams)
  - Timetable (subject-wise queries like Mathematics, Science, etc.)
  - Student analytics (count, highest marks, lowest attendance)
- Understands **different ways of asking the same question**
- Safely rejects non-document or emotional queries
- Prevents hallucination and external knowledge leakage

---

## Architecture
- **PDF Loader:** pypdf
- **Text Chunking:** Fixed-size overlapping chunks
- **Embeddings:** sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store:** FAISS
- **Retrieval Type:** Extractive RAG with intent-aware section detection
- **Answer Strategy:**
  - Intent detection
  - Semantic retrieval using embeddings
  - Section-based extraction
  - Strict document grounding

---

## Workflow
1. Extract text from the school PDF.
2. Split the text into overlapping chunks.
3. Generate embeddings and store them in a FAISS vector index.
4. When a question is asked:
   - User intent is detected even if the wording is informal.
   - Relevant document sections are retrieved using semantic similarity.
   - Only the required information is extracted and returned.
5. If the information is **not present in the PDF**, the assistant responds with:
   
   **"I don't know based on the provided documents."**

---

## How to Run

### Requirements
- Python 3.10
- Required libraries:
  - pypdf
  - sentence-transformers
  - faiss-cpu
  - numpy

### Run Command
```bash
py -3.10 school_ai_assistant.py


