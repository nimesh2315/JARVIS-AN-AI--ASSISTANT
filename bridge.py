import os
import openai
from config import api_data

openai.api_key = api_data
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-1106",
  messages=[],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)