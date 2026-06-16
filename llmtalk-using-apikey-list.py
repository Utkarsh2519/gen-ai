import os

from google import genai
from google.genai import errors

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")
client = genai.Client(api_key=api_key)

models_to_try = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-3.5-flash",
]

last_error = None
for model_name in models_to_try:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents="What is array?"
        )
        print(f"Model used: {model_name}")
        print(response.text)
        break
    except (errors.ClientError, errors.ServerError) as exc:
        last_error = exc
        print(f"{model_name} failed ({exc}). Trying the next model...")
else:
    raise RuntimeError("All fallback models are unavailable right now.") from last_error