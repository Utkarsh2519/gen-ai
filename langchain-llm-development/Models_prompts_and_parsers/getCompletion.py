
from llm_model_selector import llm_model
import openai
def get_completion(prompt, model=None):
    if model is None:
        model = llm_model
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]

get_completion("What is 1+1?")