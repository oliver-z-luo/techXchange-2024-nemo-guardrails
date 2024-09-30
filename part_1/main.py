import os
from dotenv import load_dotenv
import openai
from nemoguardrails import RailsConfig, LLMRails
from config import get_verbosity

# Load environment variables from dev.env
load_dotenv(dotenv_path="./dev.env")

# If you need to debug this script, uncomment the following lines
# and set the DEBUG environment variable to '1' in your dev.env file
if os.environ.get('DEBUG') == '1':
    import debugpy
    debugpy.listen(("localhost", 5678))
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Load GR configuration and initialize LLMRails with OpenAI
config = RailsConfig.from_path("./part_1/nemo-config")
rails = LLMRails(config)

def get_openai_completion(prompt: str):
    """
    Call the OpenAI Completion endpoint with the provided prompt.
    
    Args:
    prompt (str): The input prompt string.
    
    Returns:
    str: The completion text generated by OpenAI.
    """
    # Set the OpenAI API key
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    try:
        # Call the OpenAI completion API
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )

        # Extract and return the generated text from the response
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Start a continuous chat loop
print("===========================================")
print(" Welcome to the CLI Chat Application!")
print("===========================================\n")
print("### You can start chatting with the AI agent directly in this terminal. ###")
print("### Type 'exit' at any time to end the session. ###")
conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    conversation_history.append({"role": "user", "content": user_input})
    response = rails.generate(messages=conversation_history[-10:])
    conversation_history.append({"role": "assistant", "content": response['content']})

    print(f"Agent: {response['content']}")

    if get_verbosity():
      print("--- LLM Call Summary ---")
      info = rails.explain()
      info.print_llm_calls_summary()
      # Optionally print the conversation logic history if needed
      # print("--- Colang History ---")
      # print(info.colang_history)

print("Chat ended.")
