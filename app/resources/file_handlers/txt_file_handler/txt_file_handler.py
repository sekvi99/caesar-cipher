from dataclasses import dataclass
from ..abstract_file_handler import AbstractFileHandler
import time
 
@dataclass
class TxtFileHandler(AbstractFileHandler):
     
    def read_file(self) -> str:
        with open(self.file_path, 'r') as file:
            content = file.read()
            return content
    
    
    def write_file(self, message: str) -> None:
        with open(f'Decoded_{time.time()}', 'w') as file:
            file.write(message)