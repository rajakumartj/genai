from openai import OpenAI
from keys import Keys

client = OpenAI(api_key=Keys.OPENAI_API_KEY.value)

employee_description_function = [
    {
        'name': 'extract_employee_info',
        'description': 'Get the employee information from he body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'Employee Name': {
                    'type': 'string',
                    'description': 'Name of the employee'
                },
                'Organization Name': {
                    'type': 'string',
                    'description': 'The Organization Name'
                },
                'Division Name': {
                    'type': 'string',
                    'description': 'The Division Name'
                },
                'Manager Name': {
                    'type': 'string',
                    'description': 'The reporting Manager'
                }
            }
        }
    }
]

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
    messages=[{"role": "user", "content": prompt}],
    functions=employee_description_function
)
print(response)
print("****************************************")
print(response.choices[0].message.function_call)
print("******")
print(response.choices[0].message.function_call.arguments)
print(response.usage)
print(response.usage.prompt_tokens)
print(response.usage.completion_tokens)

