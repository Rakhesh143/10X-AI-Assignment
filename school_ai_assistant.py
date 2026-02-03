# -------------------------------------------------
# Task 3: School AI Assistant (FINAL – SAFE & STRICT)
# -------------------------------------------------

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

# -------------------------------------------------
# 1. Load PDF
# -------------------------------------------------
def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text.lower()

# -------------------------------------------------
# 2. Chunk text
# -------------------------------------------------
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# -------------------------------------------------
# 3. Build FAISS index
# -------------------------------------------------
def build_vector_store(chunks):
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embedder

# -------------------------------------------------
# 4. Student parsing
# -------------------------------------------------
def extract_students(full_text):
    pattern = re.compile(
        r"(aa\d{3})\s+([a-z ]+)\s+(\d+[a-z])\s+([a-z ]+)\s+(\d+)\s+(\d+)",
        re.MULTILINE
    )
    students = []
    for m in pattern.findall(full_text):
        students.append({
            "id": m[0],
            "name": m[1].title(),
            "class": m[2].upper(),
            "subject": m[3].title(),
            "marks": int(m[4]),
            "attendance": int(m[5])
        })
    return students

# -------------------------------------------------
# 5. Extract clean section
# -------------------------------------------------
def extract_section(chunk, title):
    if title not in chunk:
        return None

    text = chunk.split(title, 1)[1]

    stop_words = [
        "school rules",
        "fee structure",
        "exam schedule",
        "timetable",
        "student records",
        "school information"
    ]

    for stop in stop_words:
        if stop != title and stop in text:
            text = text.split(stop, 1)[0]

    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 4]
    if not lines:
        return None

    return title + ":\n" + "\n".join(lines)

# -------------------------------------------------
# 6. Answer engine (STRICT MODE)
# -------------------------------------------------
def answer_question(question, chunks, index, embedder, full_text):
    q = question.lower().strip()

    # ❌ BLOCK NON-DOCUMENT QUESTIONS
    nonsense_keywords = [
        "i love you", "love", "hi", "hello", "hey",
        "how are you", "who are you", "thank you"
    ]

    if any(k in q for k in nonsense_keywords):
        return "I don't know based on the provided documents."

    # ---- STUDENT ANALYTICS ----
    students = extract_students(full_text)

    if "how many student" in q:
        return f"There are {len(students)} students in the records."

    if "highest marks" in q:
        s = max(students, key=lambda x: x["marks"])
        return f"{s['name']} has the highest marks: {s['marks']}."

    if "lowest attendance" in q:
        s = min(students, key=lambda x: x["attendance"])
        return f"{s['name']} has the lowest attendance: {s['attendance']}%."

    # ---- INTENT DETECTION ----
    section_map = {
        "fee structure": ["fee", "tuition", "annual fee", "transport"],
        "exam schedule": ["exam", "unit test", "test", "mid", "final", "date", "when"],
        "timetable": ["timetable", "schedule", "period", "mathematics", "science"],
        "school rules": ["rule", "rules", "uniform", "mobile", "attendance"]
    }

    detected_section = None
    for section, keys in section_map.items():
        if any(k in q for k in keys):
            detected_section = section
            break

    q_embed = embedder.encode([q])
    _, indices = index.search(np.array(q_embed), k=6)

    if detected_section:
        for i in indices[0]:
            result = extract_section(chunks[i], detected_section)
            if result:
                return result

    # ❌ NO FALLBACK DUMP
    return "I don't know based on the provided documents."

# -------------------------------------------------
# MAIN
# -------------------------------------------------
if __name__ == "__main__":
    pdf_text = load_pdf_text("school_data.pdf")
    chunks = chunk_text(pdf_text)
    index, embedder = build_vector_store(chunks)

    print("School AI Assistant ready (STRICT MODE).")
    print("Answers ONLY from the PDF.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ")
        if query.lower() == "exit":
            break
        print("Answer:\n", answer_question(query, chunks, index, embedder, pdf_text))
        print()
