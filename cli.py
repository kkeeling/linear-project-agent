import sys
from colorama import init, Fore

def main():
    init()
    prompt = input(Fore.GREEN + "Please enter a prompt to write the user stories: " + Fore.RESET)
    print(Fore.BLUE + f"Received prompt: {prompt}" + Fore.RESET)

if __name__ == "__main__":
    main()
