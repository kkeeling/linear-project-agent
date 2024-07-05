import os

def read_file(file_path):
    """
    Reads the content of a file and returns it.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content
