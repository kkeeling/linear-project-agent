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

# Tool Definition
read_txt_file_tool = {
    "name": "read_txt_file",
    "description": "Read the contents of a .txt file. This tool opens and reads the specified text file, returning its contents as a string. It should be used when you need to access the content of a specific .txt file. The tool will return an error message if the file doesn't exist, isn't a .txt file, or if there are any issues reading the file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The full path to the .txt file to be read, e.g. '/path/to/file.txt'"
            }
        },
        "required": ["file_path"]
    }
}
