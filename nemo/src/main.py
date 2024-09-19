from openai import OpenAI
import os

# Access an environment variable
openai_api_key_name = "OPENAI_API_KEY"
openai_api_key = os.environ.get(openai_api_key_name)

# Use the environment variable
if openai_api_key:
    print(f"The database URL is: {openai_api_key}")
else:
    print(f"{openai_api_key_name} environment variable is not set")

# For variables that must be set, you can use os.environ[] 
# This will raise a KeyError if the variable is not set
try:
    required_var = os.environ[openai_api_key_name]
    print(f"The required variable is: {required_var}")
except KeyError:
    print(f"{openai_api_key_name} is not set in the environment")


client = OpenAI(api_key=openai_api_key)
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

message = response.choices[0].message.content
print(message)