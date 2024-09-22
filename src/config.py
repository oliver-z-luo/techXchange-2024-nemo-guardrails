import os

def get_openai_api_key():
  """Retrieves the OpenAI API key from the environment variable.

  Returns:
      str: The OpenAI API key, or None if it's not set.
  """

  openai_api_key_name = "OPENAI_API_KEY"
  try:
    os.environ[openai_api_key_name]
    openai_api_key = os.environ.get(openai_api_key_name)
    return openai_api_key
  except KeyError:
      print(f"{openai_api_key_name} is not set in the environment")
