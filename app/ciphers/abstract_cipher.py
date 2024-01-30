from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AbstractCipher(ABC):
    message: str # * String representation of message to code/ decode
    
    @abstractmethod
    def code_message(self) -> str:
        """
        Method should code message, using implemented cipher.

        Returns:
            str: String representation of encoded message.
        """
        ...
        
    @abstractmethod
    def decode_message(self) -> str:
        """
        Method should decode message, using implemented cipher.

        Returns:
            str: String representation of decoded message.
        """
        ...
        
    @abstractmethod
    def force_message_decode(self) -> Any:
        """
        Method should try to decode message without knowing message code pattern.

        Returns:
            Any: Any representation of decoded message.
        """
        ...