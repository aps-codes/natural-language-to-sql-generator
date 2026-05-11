from google import genai
from dotenv import load_dotenv
import os

# load env
load_dotenv()

# api key
api_key = os.getenv("GOOGLE_API_KEY")

# client
client = genai.Client(api_key=api_key)

# response
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain SQL in one simple sentence."
)

print(response.text)