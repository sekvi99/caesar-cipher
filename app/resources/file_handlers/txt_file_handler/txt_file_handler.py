from dataclasses import dataclass
from ..abstract_file_handler import AbstractFileHandler
import time
 
@dataclass
class TxtFileHandler(AbstractFileHandler):
     
    def read_file(self) -> str:
        """
        Function to read from provided file path.

        Returns:
            str: String representation of file content.
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
            return content
    
    
    def write_file(self, message: str) -> None:
        """
        Function to wrtie to provided file.

        Args:
            message (str): String representation of message to save.
        """
        with open(f'Decoded_{time.time()}', 'w') as file:
            file.write(message)