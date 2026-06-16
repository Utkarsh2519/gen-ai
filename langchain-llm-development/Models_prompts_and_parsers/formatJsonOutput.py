import openai_config 
customer_review = """\
This leaf blower is pretty amazing. It has four settings: \
candle blower, gentle breeze, windy city, and tornado. \
It arrived in two days, just in time for my wife's \
anniversary present. \
I think my wife liked it so much she was speechless. \
So far I've been the only one using it, and I've been \
using it every other morning to clear the leaves on our lawn. \
It's slightly more expensive than the other leaf blowers \
out there, but I think it's worth it for the extra features.
"""

review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? Answer True or False.
delivery_days: How many days did it take for the product to arrive?
price_value: Extract any sentences about the value or price.

Format the output as JSON with the following keys:
gift
delivery_days
price_value

text: {text}
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from llm_model_selector import llm_model

prompt_template = ChatPromptTemplate.from_template(review_template)
print(prompt_template)
messages = prompt_template.format_messages(text=customer_review)
chat = ChatOpenAI(temperature=0.0, model=llm_model())
response = chat(messages)
print("*************************************************************")
print(response.content)