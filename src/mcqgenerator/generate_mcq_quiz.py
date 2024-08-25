from keys import Keys
import os
from dotenv import load_dotenv
import json
import pandas as pd
from os.path import dirname, join



import traceback
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.callbacks.manager import get_openai_callback
from langchain.chains import SequentialChain

load_dotenv()
KEY = os.getenv("OPENAI_API_KEY")

project_root = dirname(dirname(__file__))
output_path = join(project_root, 'json_files/mcq_output.json')

TEMPLATE = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure that the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
"""

TEMPLATE2 = """
You are an expert English grammarian and writer. Given a multiple choice quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words
for complexity if the quiz is not as per with the cognitive and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}
check for an expert writer of the above quiz:
"""

f = open(output_path)
RESPONSE_JSON = json.load(f)
json.dumps(RESPONSE_JSON)

quiz_generation_prompt = PromptTemplate(
    input_variables=["name", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-3.5-turbo", temperature=0.5)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=TEMPLATE2
)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# Connect both the chains using Sequential chains
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain],
                                          input_variables=["text", "number", "subject", "tone", "response_json"],
                                          output_variables=["quiz", "review"], verbose=True
                                          )

# file_path = r"./genai\src\input_data\mcq_quiz_data.txt"
file_path = join(project_root, 'input_data\mcq_quiz_data.txt')

with open(file_path, 'r') as file:
    TEXT = file.read()

NUMBER = 5
SUBJECT = "Machine Learning"
TONE = "simple"

with get_openai_callback() as cb:
    response = generate_evaluate_chain(
        {
            "text": TEXT,
            "number": NUMBER,
            "subject": SUBJECT,
            "tone": TONE,
            "response_json": json.dumps(RESPONSE_JSON)
        }
    )

print(f"Total Tokens: {cb.total_tokens}")
print(f"Prompt Token: {cb.prompt_tokens}")
print(f"Completion Tokens: {cb.completion_tokens}")
print(f"Total Cost: {cb.total_cost}")

# print(response.get("quiz"))
quiz = response.get("quiz")

quiz = json.loads(quiz)

quiz_table_data = []
for key, value in quiz.items():
    mcq = value["mcq"]
    options = "|".join(
        [
            f"{option}:{option_value}"
            for option, option_value in value["options"].items()
        ]
    )
    correct = value["correct"]
    quiz_table_data.append({"MCQ": mcq, "choices": options, "Correct": correct})
print(quiz_table_data)

quiz_data_frame = pd.DataFrame(quiz_table_data)
print(quiz_data_frame)
quiz_data_frame.to_csv("quiz_msq.csv", index=False)
