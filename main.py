from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 読み込み
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="おはよう"
)

print(response.output_text)
