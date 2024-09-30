from nemoguardrails import RailsConfig, LLMRails
from config import get_verbosity

config = RailsConfig.from_path("./part_1/nemo-config")
rails = LLMRails(config)

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

    if get_verbosity():
      print("--- LLM Call Summary ---")
      info = rails.explain()
      info.print_llm_calls_summary()
      # Optionally print the conversation logic history if needed
      # print("--- Colang History ---")
      # print(info.colang_history)
    
    print(f"Agent: {response['content']}")

print("Chat ended.")
