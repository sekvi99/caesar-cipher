import os
from app.models.property_messages import ExceptionMessages, UserOptions, ProgramStartOptions
from app.resources.file_handlers.txt_file_handler.txt_file_handler import TxtFileHandler
from app.ciphers.caesar_cipher.caesar_cipher import CaesarCipher
import json
import time

def enter_option() -> str:
    """
    Helper function to get choosen option from user. 

    Returns:
        str: String representation of choosen user option.
    """
    while True:
        option = input("Enter option number: ")
        if option in [UserOptions.MESSAGE.value, UserOptions.FILE_PATH.value]:
            return option
        else:
            print(ExceptionMessages.OPTION_NOT_FOUND.value)

def enter_start_option() -> str:
    while True:
        option = input("Enter option number: ")
        if option in [ProgramStartOptions.ENCODE.value, ProgramStartOptions.DECODE.value, ProgramStartOptions.FORCE_DECODE.value]:
            return option
        else:
            print(ExceptionMessages.OPTION_NOT_FOUND.value)

def enter_message() -> str:
    """
    Helper function to generate input for getting message from user.
    
    Returns:
        str: String representation of user provided message.
    """
    message = input("Enter message to encode: ")
    return message
    
def provide_file_path() -> str:
    """
    Helper function to get file path from user.
    
    Returns:
        str: String representation of file path in system.
    """
    while True:
        file_path = input("Enter the file path: ")
        if os.path.exists(file_path):
            return file_path
        else:
            print(ExceptionMessages.FILE_NOT_FOUND)

def generate_script_options() -> None:
    """
    Helper function to generate script description.
    """
    print("Choose an option")
    print("1. Encode message")
    print("2. Decode message")
    print("3. Force script to decode")

def generate_encode_description() -> None:
    """
    Helper function to generate options to encode/decode description.
    """
    print("Choose an option")
    print("1. Enter a message")
    print("2. Provide a file path")
    
def get_shift_input() -> int:
    """
    Helper function for getting shift required to code/ decode messages.

    Returns:
        int: Numerical representation of shift for cipher.
    """
    while True:
        try:
            shift = int(input("Enter the shift value for the Caesar cipher: "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Please enter a valid integer.")
    

def process_user_input() -> None:
    """
    Helper function to generate script flow.
    """
    generate_script_options()
    user_option = enter_start_option()

    generate_encode_description()
    encode_option = enter_option()

    if encode_option == "1":
        message = enter_message()
    else:
        file_path = provide_file_path()

    txt_file_handler = TxtFileHandler(file_path) if encode_option == "2" else None
    file_content = txt_file_handler.read_file() if txt_file_handler else None

    caesar_cipher = CaesarCipher(message) if encode_option == "1" else CaesarCipher(file_content)
    
    if user_option == ProgramStartOptions.ENCODE.value:
        shift = get_shift_input()
        print(f"Your coded message using Caesar Cipher with shift: {shift}")
        print(caesar_cipher.code_message(shift))
        
    elif user_option == ProgramStartOptions.DECODE.value:
        shift = get_shift_input()
        print(f"Your uncoded message using Caesar Cipher and shift: {shift}")
        print(caesar_cipher.decode_message(shift))
        
    elif user_option == ProgramStartOptions.FORCE_DECODE.value:
        print("Your uncoded message options using Caesar Cipher")
        options = caesar_cipher.force_message_decode()
        print(options)

        if encode_option == "2":
            with open(f"Results_{time.time()}.json", 'w') as json_file:
                json.dump(options, json_file, indent=4)
        
        
        
        
    