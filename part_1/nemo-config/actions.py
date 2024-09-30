from nemoguardrails.actions import action
from openai import OpenAI
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
client = OpenAI()

from part_1.config import get_verbosity

# Helper function to call the OpenAI API and parse the result
async def call_openai_api(prompt: str, bot_response: str) -> bool:
    """
    Calls the OpenAI API and returns True if the answer is 'yes', otherwise False.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=90
    ).to_dict()
    
    response_content = response['choices'][0]['message']['content'].strip().lower()
    result = json.loads(response_content)

    if get_verbosity():
      print(f"--- Output Guardrail Results ---")
      print(f"Respond evaluated:  {bot_response}")
      print(f"Contains:           {result['answer']}")
      print(f"Rationale:          {result['rationale']}")
    return result['answer'] == "yes"

@action(name="self_check_quotes")
async def self_check_quotes(bot_response: str):
    """
    Async function that calls OpenAI API and checks if the bot response mentions quotes or quotations.
    Returns True if it contains, False otherwise.
    """

    prompt_quote = f"""
    Does the following text explicitly mention quotations or quotes?
    
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

@action(name="self_check_sales")
async def self_check_sales(bot_response: str):
    """
    Async function that calls OpenAI API and checks if the bot response mentions selling a product/service.
    Returns True if it contains, False otherwise.
    """

    prompt_sales = f"""
    Does the following text explicitly mention sales?
    
    ## Start of Text ##
    {bot_response}
    ## End of Segment ##

    Respond in JSON format:
    {{
      "answer": "yes" | "no",
      "rationale": "string" # short explanation of answer
    }}
    """
    return await call_openai_api(prompt_sales, bot_response)
