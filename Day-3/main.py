from ai_service import ask_ai

question = input("Ask your question: ")

answer = ask_ai(question)

print("\nAI Answer:\n")
print(answer)