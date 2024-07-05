import sys
from colorama import init, Fore

def main():
    init()
    print(Fore.YELLOW + "Hello! I am your user story generation agent. I help you create user stories based on the prompts you provide." + Fore.RESET)
    prompt = input(Fore.GREEN + "\nPlease enter a prompt to write the user stories: " + Fore.RESET)
    print(Fore.BLUE + f"Received prompt: {prompt}" + Fore.RESET)

if __name__ == "__main__":
    main()
