from google import genai

api_key = open('.gemini-api-key').read().strip()

client = genai.Client(
    api_key=api_key
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
