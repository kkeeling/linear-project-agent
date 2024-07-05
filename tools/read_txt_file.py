import os

def read_txt_file(file_path):
    """
    Opens a .txt file and returns its contents.
    """
    try:
        # Check if the file has a .txt extension
        if not file_path.lower().endswith('.txt'):
            return f"Error: File '{file_path}' is not a .txt file."

        # Check if the file exists
        if not os.path.exists(file_path):
            return f"Error: File not found at path '{file_path}'"

        # Read the contents of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError as e:
        return f"Error reading file: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Tool definition for Claude
read_txt_file_tool = {
    "type": "function",
    "function": {
        "name": "read_txt_file",
        "description": "Read the contents of a .txt file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the .txt file to be read"
                }
            },
            "required": ["file_path"]
        }
    }
}