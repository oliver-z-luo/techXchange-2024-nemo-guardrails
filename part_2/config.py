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

def get_verbosity():
  verbosity_name = "CHATBOT_VERBOSITY"
  try: 
    os.environ[verbosity_name]
    verbosity_setting = os.environ.get(verbosity_name)
    if verbosity_setting == 1 or verbosity_setting == "1":
      return True
    else:
      return False
  except KeyError:
      print(f"{verbosity_name} is not set in the environment")
