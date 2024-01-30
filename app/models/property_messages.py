from enum import Enum


class ExceptionMessages(Enum):
    SHIFT_NOT_A_NUMBER = "Shift must be a number."
    INVALID_INPUT = "Invalid input provided."
    DIVISION_BY_ZERO = "Cannot divide by zero."
    FILE_NOT_FOUND = "File not found."
    OPTION_NOT_FOUND = "Option not found."
    
class UserOptions(Enum):
    MESSAGE = "1"
    FILE_PATH = "2"
    
class ProgramStartOptions(Enum):
    ENCODE = "1"
    DECODE = "2"
    FORCE_DECODE = "3"