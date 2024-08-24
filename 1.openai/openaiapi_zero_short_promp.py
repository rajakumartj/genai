from openai import OpenAI

my_api_key = ""
client = OpenAI(api_key=my_api_key)
my_prompt = "How to pass UPSC exam?"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": my_prompt
        }
    ],
    max_tokens=200
)
# print(response)
print("****************************************")
print(response.choices[0].message.content)
print(response.usage)
print(response.usage.prompt_tokens)
print(response.usage.completion_tokens)
# usage=CompletionUsage(completion_tokens=200, prompt_tokens=14, total_tokens=214))
