from enum import Enum

class ExceptionMessages(Enum):
    SHIFT_NOT_A_NUMBER = "Shift must be a number."
    INVALID_INPUT = "Invalid input provided."
    DIVISION_BY_ZERO = "Cannot divide by zero."
    FILE_NOT_FOUND = "File not found."