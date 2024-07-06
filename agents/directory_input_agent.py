import os
import os
from colorama import init, Fore, Style

class DirectoryInputAgent:
    def __init__(self):
        self.directory = None
        self.files_contents = {}

    def ask_for_directory(self):
        # Initialize colorama
        init()

        while True:
            directory = input(f"{Fore.GREEN}Agent: Please enter the local directory where project files can be found: {Style.RESET_ALL}")
            if directory.lower() == 'exit':
                print(f"{Fore.GREEN}Agent: Exiting directory input.{Style.RESET_ALL}")
                break
            elif os.path.isdir(directory):
                self.directory = directory
                print(f"{Fore.GREEN}Agent: Directory exists: {directory}{Style.RESET_ALL}")
                self.read_files_in_directory()
                
                break
            else:
                print(f"{Fore.RED}Agent: Error: The directory '{directory}' does not exist. Please try again.{Style.RESET_ALL}")
        return self.directory

    def read_files_in_directory(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    self.files_contents[file_path] = f.read()
        print(f"{Fore.GREEN}Agent: Successfully loaded {len(self.files_contents)} files from the directory.{Style.RESET_ALL}")
