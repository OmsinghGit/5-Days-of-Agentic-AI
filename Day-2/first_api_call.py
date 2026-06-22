import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print(os.getenv("NVIDIA_API_KEY"))

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Explain Binary Search in simple terms for a beginner engineering student."
        }
    ]
)

print(response.choices[0].message.content)