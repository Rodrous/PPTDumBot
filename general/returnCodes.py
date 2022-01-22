from enum import Enum, auto


class ReturnCode(Enum):
    Success = auto()
    Unchanged = auto()
    Fail = auto()
