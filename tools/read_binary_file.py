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

# Tool Definition
read_binary_file_tool = {
    "name": "read_binary_file",
    "description": "Reads a binary file and returns its metadata and base64-encoded content. This tool should be used when you need to access the contents of a binary file, such as an image, audio file, or any non-text file. It provides the file's name, size, type, and the actual content encoded in base64 format. The tool is useful for tasks that require processing or analyzing binary data. Note that this tool does not interpret or modify the file contents; it simply reads and encodes the raw binary data.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The full path to the binary file to be read, e.g., '/path/to/image.jpg' or 'C:\\Documents\\audio.mp3'"
            }
        },
        "required": ["file_path"]
    }
}
