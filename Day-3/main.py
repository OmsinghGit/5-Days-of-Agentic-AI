from ai_service import ask_ai

question = input("Ask your study question: ")

answer = ask_ai(question)

print("\nAI Answer:\n")
print(answer)