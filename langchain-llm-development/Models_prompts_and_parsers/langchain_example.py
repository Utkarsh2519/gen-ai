from llm_model_selector import llm_model
from langchain_openai import ChatOpenAI


chat = ChatOpenAI(temperature=0.0, model=llm_model())

# Example usage
response = chat.predict("What is 1+1?")
print(response)