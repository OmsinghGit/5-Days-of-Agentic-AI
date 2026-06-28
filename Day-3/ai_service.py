from openai import OpenAI, OpenAIError
from config import API_KEY

from prompts import (
    GENERAL_PROMPT,
    PROGRAMMING_PROMPT,
    COMPARISON_PROMPT,
    FACT_PROMPT
)

# Initialize client only if API_KEY is provided
client = None
if API_KEY:
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=API_KEY
    )


def ask_ai(question):
    global client

    if not API_KEY or not client:
        return "Error: NVIDIA_API_KEY is missing or invalid. Please check your config.py and .env file configuration."

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

    try:
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

        if not response.choices:
            return "Error: The AI returned an empty response."

        return response.choices[0].message.content

    except OpenAIError as e:
        return f"API Error: Failed to communicate with NVIDIA NIM API. Details: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: An error occurred while retrieving answer. Details: {str(e)}"


