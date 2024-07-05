def read_file(file_path):
    """
    Opens a text file and returns its contents.

    Args:
    file_path (str): The path to the text file to be read.

    Returns:
    str: The contents of the file as a string.

    Raises:
    FileNotFoundError: If the specified file is not found.
    IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File not found at path '{file_path}'"
    except IOError as e:
        return f"Error reading file: {str(e)}"

# Tool Definition
read_file_tool = {
    "name": "read_file",
    "description": "Opens a text file and returns its contents. Use this tool when you need to read the content of a specific text file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to the text file to be read."
            }
        },
        "required": ["file_path"]
    }
}