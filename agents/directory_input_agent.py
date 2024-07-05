from colorama import init, Fore, Style

class DirectoryInputAgent:
    def ask_for_directory(self):
        # Initialize colorama
        init()

        directory = input(f"{Fore.CYAN}Please enter the local directory where project files can be found: {Style.RESET_ALL}")
        return directory

if __name__ == "__main__":
    agent = DirectoryInputAgent()
    directory = agent.ask_for_directory()
    print(f"Directory entered: {directory}")
