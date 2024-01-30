from dataclasses import dataclass
from typing import Dict
from app.ciphers.abstract_cipher import AbstractCipher

@dataclass(frozen=True)
class CaesarCipher(AbstractCipher):
        
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
    
    def decode_message(self, shift: int) -> str:
        """
        Overwritten method that decodes message using caesar cipher.

        Returns:
            str: String representation of decoded message.
        """
        return self.code_message(-shift)
    
    def force_message_decode(self) -> Dict[str, str]:
        """
        Attempt to decode the message without knowing the shift.

        Returns:
            Dict[str, str]: Dictionary representation of the decoded message.
        """
        return { f'SHIFT_{possible_shift}' : self.code_message(possible_shift) for possible_shift in range(26) }