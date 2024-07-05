class DirectoryInputAgent:
    def ask_for_directory(self):
        directory = input("Please enter the local directory where project files can be found: ")
        return directory

if __name__ == "__main__":
    agent = DirectoryInputAgent()
    directory = agent.ask_for_directory()
    print(f"Directory entered: {directory}")
