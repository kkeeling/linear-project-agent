from colorama import init, Fore, Style

class DirectoryInputAgent:
    def __init__(self):
        self.directory = None

    def ask_for_directory(self):
        # Initialize colorama
        init()

        directory = input(f"{Fore.CYAN}Please enter the local directory where project files can be found: {Style.RESET_ALL}")
        self.directory = directory
        return self.directory

