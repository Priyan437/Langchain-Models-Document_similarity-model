

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

print("TOKEN =", os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

response = client.chat.completions.create(
    model="Qwen/Qwen3-32B",
    messages=[
        {
            "role": "user",
            "content": "Who is the Prime Minister of India?"
        }
    ]
)

print(response.choices[0].message.content)