from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 読み込み
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "次の画像について説明してください。",
                },
                {
                    "type": "input_image",
                    "image_url": "https://i.imgur.com/4AiXzf8.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)
