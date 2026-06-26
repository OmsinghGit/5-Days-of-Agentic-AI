from openai import OpenAI
from config import API_KEY

from prompts import (
    GENERAL_PROMPT,
    PROGRAMMING_PROMPT,
    COMPARISON_PROMPT,
    FACT_PROMPT
)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)


def ask_ai(question):

    question_lower = question.lower()

    if "difference" in question_lower or "compare" in question_lower:
        selected_prompt = GENERAL_PROMPT + "\n" + COMPARISON_PROMPT

    elif any(word in question_lower for word in [
        "capital",
        "inventor",
        "scientific name",
        "who is",
        "what is the"
    ]):
        selected_prompt = GENERAL_PROMPT + "\n" + FACT_PROMPT

    else:
        selected_prompt = GENERAL_PROMPT + "\n" + PROGRAMMING_PROMPT

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        messages=[
            {
                "role": "system",
                "content": selected_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content