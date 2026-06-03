from services.llm import llm

response = llm.invoke(
    "What is a startup in one sentence?"
)
print("Working...")
print(response.content)