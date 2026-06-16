import os
from google import genai

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")
client = genai.Client(api_key=api_key)
history=[]
while(True):
    userProblem = input("Ask me anything: ")
    history.append({"role": "user", "parts": [{"text": userProblem}]},)
    if userProblem != "bye":
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=history
        )
        print(response.text)
        history.append({"role": "model", "parts": [{"text": response.text}]})
    else:
        print("it was nice talking to you")
        break