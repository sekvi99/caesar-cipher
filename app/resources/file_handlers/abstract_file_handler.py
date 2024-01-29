from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.models.property_messages import ExceptionMessages
import os

@dataclass
class AbstractFileHandler(ABC):
    _file_path: str
    
    @property
    def file_path(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self._file_path
    
    @property.setter
    def file_path(self, value: str) -> str:
        """_summary_

        Args:
            value (str): _description_

        Returns:
            str: _description_
        """
        if not os.path.exists(value):
            raise FileNotFoundError(ExceptionMessages.FILE_NOT_FOUND)

        self._file_path = value
                
    @abstractmethod
    def read_file(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        ...
        
    @abstractmethod
    def write_file(self, message: str) -> None:
        """
        
        """
        ...
    
