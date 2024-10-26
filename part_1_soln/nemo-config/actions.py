from nemoguardrails.actions import action
from openai import OpenAI
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
client = OpenAI()

from part_1.config import get_verbosity

async def call_openai_api(prompt: str, bot_response: str) -> bool:
  """
  Calls the OpenAI API with the given prompt and bot response. 
  Returns True if the API's answer is 'yes', otherwise False.
  """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "system", "content": prompt}],
      max_tokens=90
  ).to_dict()

  response_content = response['choices'][0]['message']['content'].strip().lower()

  try:
      result = json.loads(response_content)
  except json.JSONDecodeError:
      if get_verbosity():
          print(f"Error: Response content is not valid JSON: {response_content}")
      return False

  if get_verbosity():
      print(f"--- Output Guardrail Results ---")
      print(f"Response evaluated: {bot_response}")
      print(f"Contains:           {result.get('answer', 'output error by model')}")
      print(f"Rationale:          {result.get('rationale', 'output error by model')}")

  return result.get('answer', '') == "yes"
    

@action(name="self_check_quotes")
async def self_check_quotes(bot_response: str):
  """
  Async function that calls OpenAI API and checks if the bot response mentions quotes or quotations.
  Returns True if it contains, False otherwise.
  """

  prompt_quote = f"""
  Does the following text explicitly mention any actions related to quote management, such as generating, updating, or handling quotations or quotes in any form?
  
  ## Start of Text ##
  {bot_response}
  ## End of Text ##

  Respond only in valid JSON format (no markdown):
  {{
    "answer": "yes" | "no",
    "rationale": "string" # short explanation of answer
  }}
  """
  return await call_openai_api(prompt_quote, bot_response)

@action(name="self_check_deals")
async def self_check_deals(bot_response: str):
  """
  Async function that calls OpenAI API and checks if the bot response mentions selling a product/service.
  Returns True if it contains, False otherwise.
  """

  prompt_deals = f"""
  Does the following text explicitly mention business transactions or negotiations, including but not limited to:
  - Negotiating terms, prices, or conditions
  - Agreeing to or closing business deals
  - Discussing contracts or agreements
  
  ## Start of Text ##
  {bot_response}
  ## End of Segment ##

  Respond in JSON format (no markdown):
  {{
    "answer": "yes" | "no",
    "rationale": "string" # short explanation of answer
  }}
  """
  return await call_openai_api(prompt_deals, bot_response)
