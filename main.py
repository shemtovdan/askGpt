from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

print("Pose moi une quetion ?")

questionUser = input()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Repond moi une phrase et en français."},
    {"role": "user", "content": questionUser}
  ]
)
print(completion.choices[0].message.content)
