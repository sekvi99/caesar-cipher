import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.models.property_messages import \
    ExceptionMessages  # Assuming you have an ExceptionMessages module


@dataclass
class AbstractFileHandler(ABC):
    _file_path: str
    
    @property
    def file_path(self) -> str:
        """Get the file path.

        Returns:
            str: The file path.
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self, value: str) -> None:
        """Set the file path.

        Args:
            value (str): The new file path.

        Raises:
            FileNotFoundError: If the specified file path does not exist.
        """
        if not os.path.exists(value):
            raise FileNotFoundError(ExceptionMessages.FILE_NOT_FOUND)

        self._file_path = value
                
    @abstractmethod
    def read_file(self) -> str:
        """Read the contents of the file.

        Returns:
            str: The contents of the file.
        """
        ...
        
    @abstractmethod
    def write_file(self, message: str) -> None:
        """Write the given message to the file.

        Args:
            message (str): The message to write to the file.
        """
        ...