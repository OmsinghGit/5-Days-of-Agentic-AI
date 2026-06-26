from prompts import SYSTEM_PROMPT

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

    return response.choices[0].message.content