import os
from colorama import init, Fore, Style

class DirectoryInputAgent:
    def __init__(self):
        self.directory = None

    def ask_for_directory(self):
        # Initialize colorama
        init()

        directory = input(f"{Fore.CYAN}Please enter the local directory where project files can be found: {Style.RESET_ALL}")
        if os.path.isdir(directory):
            self.directory = directory
            print(f"{Fore.GREEN}Directory exists: {directory}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Error: The directory '{directory}' does not exist.{Style.RESET_ALL}")
            self.directory = None
        return self.directory

