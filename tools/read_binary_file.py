import base64
import os

def read_binary_file(file_path):
    """
    Opens a binary file and returns its contents as a base64-encoded string.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        file_type = os.path.splitext(file_name)[1].lower()

        with open(file_path, 'rb') as file:
            binary_content = file.read()

        base64_content = base64.b64encode(binary_content).decode('utf-8')

        return {
            'content': base64_content,
            'file_name': file_name,
            'file_size': file_size,
            'file_type': file_type
        }
    except FileNotFoundError as e:
        return {'error': str(e)}
    except IOError as e:
        return {'error': f"Error reading file: {str(e)}"}
    except Exception as e:
        return {'error': f"Unexpected error: {str(e)}"}

# Tool definition for Claude
read_binary_file_tool = {
    "type": "function",
    "function": {
        "name": "read_binary_file",
        "description": "Read a binary file and return its metadata and base64-encoded content",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the binary file to be read"
                }
            },
            "required": ["file_path"]
        }
    }
}