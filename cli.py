import os
from dotenv import load_dotenv
from claude_chat_agent import ClaudeChatAgent
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

    chat_agent = ClaudeChatAgent(api_key)

    print(f"{Fore.CYAN}Welcome to the AI Chat Agent!")
    print(f"{Fore.CYAN}You can chat with me or ask about reading files. Just speak naturally!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type 'exit' to end the chat.{Style.RESET_ALL}")

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
