

from enum import Enum

class Modes(Enum):
    NORMAL = "normal"
    MATEMATICAS = "matemáticas"
    PERSONAL = "personal"
    TICTACTOE = "tictactoe"
    TEST_TURING = "test_turing"
    def __str__(self):
        return self.value


print(Modes.NORMAL)
