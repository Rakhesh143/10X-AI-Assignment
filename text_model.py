from transformers import pipeline

model = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

question = input("Enter your question: ")

result = model(
    question,
    max_new_tokens=200,
    do_sample=False
)

print("\nOutput:")
print(result[0]["generated_text"])
