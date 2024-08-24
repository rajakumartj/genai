
from openai import OpenAI
import os
import pandas as pd

client = OpenAI(
    # This is default and can be omitted
    api_key=os.environ.get("OPEN_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system",
            "content": "you are a helpful"
        },

        {
            "role": "user",
            "content":"How I can make a money?"
        },
        {
            "role":"assistant",
            "content":"There are a many ways to make money,and it is ultimately depends on your skills"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)