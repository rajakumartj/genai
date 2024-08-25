from keys import Keys
from openai import OpenAI


client = OpenAI(api_key=Keys.OPENAI_API_KEY.value)

employee_description = "Rajakumar is working for Morgan stanley in Wealth management division reporting to Ashish and workiing on RMT application"
prompt = f'''
Please extract the following information from the given text and return it as a JSON object:

Employee Name
Organization Name
Division Name
Reporting Manager

This is the body of the text to extract the information from:
{employee_description}
'''

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=200
)
print(response)
print("****************************************")
print(response.choices[0].message.content)
print(response.usage)
print(response.usage.prompt_tokens)
print(response.usage.completion_tokens)

