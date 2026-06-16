from google import genai

client = genai.Client(api_key="REDACTED")
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