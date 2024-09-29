from nemoguardrails.actions import action
from openai import OpenAI
client = OpenAI()

@action(name="self_check_quotes")
async def self_check_quotes(bot_response: str):
    """
    Async function that calls OpenAI API and checks if the bot response mentions quotes or quotations.
    Returns True if it contains, False otherwise.
    """
    # OpenAI API call to check for quotes or quotations in the bot response
    print(f"Bot Response: {bot_response}")
    prompt = f"""
    Model_output: {bot_response}

    Does this directly mention quotations or quotes?

    Answer [Yes/No]:
    """
    # Assuming the completion call to OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Replace with the correct model if necessary
        messages=[{"role": "system", "content": prompt}],
        max_tokens=10
    )
    
    # Extract the answer from the API response and check if it contains "Yes" or "No"
    result = response.choices[0].message.content.strip().lower()
    
    # Return True for "Yes" and False for "No"
    print(f"quotes result: {result}")
    return result == "yes"

@action(name="self_check_sales")
async def self_check_sales(bot_response: str):
    """
    Async function that calls OpenAI API and checks if the bot response mentions selling a product/service.
    Returns True if it contains, False otherwise.
    """
    # OpenAI API call to check for sales or selling-related content
    prompt = f"""
    Model_output: {bot_response}

    Does this directly mention selling a product/service?

    Answer [Yes/No]:
    """
    # Assuming the completion call to OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Replace with the correct model if necessary
        messages=[{"role": "system", "content": prompt}],
        max_tokens=90
    )
    
    # Extract the answer from the API response and check if it contains "Yes" or "No"
    result = response.choices[0].message.content.strip().lower()
    print(f"sales result: {result}")
    # Return True for "Yes" and False for "No"
    return result == "yes"