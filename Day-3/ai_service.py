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

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )


    print(response.choices[0].message)

    return response.choices[0].message.content