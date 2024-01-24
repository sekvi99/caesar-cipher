from dataclasses import dataclass
from typing import Any
from abstract_cipher import AbstractCipher
from app.models.property_messages import ExceptionMessages

@dataclass(frozen=True)
class CaesarCipher(AbstractCipher):
    _shift: int
    
    @property
    def shift(self) -> int:
        """
        Property getter for shift.

        Returns:
            int: Number representation of shift property.
        """
        return self._shift

    @shift.setter
    def shift(self, value: int) -> None:
        """
        Property setter for shift.

        Args:
            value (int): Number representation of value to set.

        Raises:
            ValueError: Occures when provided value was not an int instance.
        """
        if not isinstance(value, int):
            raise ValueError(ExceptionMessages.SHIFT_NOT_A_NUMBER)
        self._shift = value
        
    def code_message(self, shift: int) -> str:
        """
        Overwritten method that codes message using caesar cipher.

        Returns:
            str: Returns string representation of encoded message.
        """
        encrypted_message = ""
        for char in self.message:
            if char.isalpha():
                # Preserve the case of the character
                base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
                encrypted_message += encrypted_char
            else:
                # Leave non-alphabetic characters unchanged
                encrypted_message += char
        return encrypted_message
    
    def decode_message(self) -> str:
        """
        Overwritten method that decodes message using caesar cipher.

        Returns:
            str: String representation of decoded message.
        """
        return self.code_message(self.message, -self.shift)
    
    def force_message_decode(self) -> Any:
        """
        Attempt to decode the message without knowing the shift.

        Returns:
            str: String representation of the decoded message.
        """
        return { f'SHIFT_{possible_shift}' : self.code_message(possible_shift) for possible_shift in range(26) }