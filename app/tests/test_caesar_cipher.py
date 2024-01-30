from app.ciphers.caesar_cipher.caesar_cipher import CaesarCipher
import pytest

@pytest.fixture
def caesar_cipher():
    return CaesarCipher("Hello, World!")

def test_code_message(caesar_cipher):
    # Test encoding message with a shift of 3
    encoded_message = caesar_cipher.code_message(3)
    assert encoded_message == "Khoor, Zruog!"

def test_decode_message(caesar_cipher):
    # Test decoding message with a shift of 3
    decoded_message = caesar_cipher.decode_message(3)
    assert decoded_message == "Hello, World!"

def test_force_message_decode(caesar_cipher):
    # Test force message decode
    decoded_messages = caesar_cipher.force_message_decode()
    
    # Check if all 26 possible shifts are generated
    assert len(decoded_messages) == 26
    
    # Check if decoding and encoding with each shift results in the original message
    for shift, decoded_message in decoded_messages.items():
        encoded_message = caesar_cipher.code_message(int(shift.split('_')[1]))
        assert decoded_message == encoded_message