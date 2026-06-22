from openai import OpenAI
from config import API_KEY

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
        "content": """
        You are an AI Study Assistant.

        Explain concepts in simple language.
        Use examples.
        Give interview tips.
        Provide code when needed.
        End with a short summary.
        """
    },
    {
        "role": "user",
        "content": question
    }
]
    )

    return response.choices[0].message.content