import os
from dotenv import load_dotenv
from claude_chat_agent import ClaudeChatAgent
from agents.directory_input_agent import DirectoryInputAgent
from tools.read_txt_file import read_txt_file_tool
from tools.read_binary_file import read_binary_file_tool
from colorama import init, Fore, Style
from yaspin import yaspin
from yaspin.spinners import Spinners

def main():
    # Initialize colorama
    init()

    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print(f"{Fore.RED}Error: ANTHROPIC_API_KEY not found in environment variables.{Style.RESET_ALL}")
        return

    directory_agent = DirectoryInputAgent()
    directory_agent.ask_for_directory()
    document_data = directory_agent.files_contents

    chat_agent = ClaudeChatAgent(api_key, document_data=document_data)

    print(f"{Fore.GREEN}Agent: Welcome to the Linear Project Agent!")
    print(f"{Fore.GREEN}Agent: Would you like me to generate a list of user stories and tasks for you? I will base my work on the files in your directory. [Y/N]{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Agent: At any time, you can type 'exit' to end the chat.{Style.RESET_ALL}")

    initial_response = input(f"\n{Fore.YELLOW}You: {Style.RESET_ALL}").strip()

    if initial_response.lower() == 'n':
        print(f"{Fore.GREEN}Agent: Goodbye!{Style.RESET_ALL}")
        return

    while True:
        user_input = input(f"\n{Fore.YELLOW}You: {Style.RESET_ALL}").strip()

        if user_input.lower() == 'exit':
            print(f"{Fore.GREEN}Agent: Goodbye! It was nice chatting with you.{Style.RESET_ALL}")
            break

        with yaspin(Spinners.dots12, text="Thinking...", color="cyan") as spinner:
            response = chat_agent.chat(user_input)
            spinner.ok("✓")

        print(f"{Fore.GREEN}Agent: {response}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
