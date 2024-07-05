import os
from dotenv import load_dotenv
from claude_chat_agent import ClaudeChatAgent
from tools.read_txt_file import read_txt_file_tool
from tools.read_binary_file import read_binary_file_tool

def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        return

    chat_agent = ClaudeChatAgent(api_key)

    print("Welcome to the AI Chat Agent!")
    print("You can chat with me or ask about reading files. Just speak naturally!")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'exit':
            print("AI: Goodbye! It was nice chatting with you.")
            break

        response = chat_agent.chat(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()