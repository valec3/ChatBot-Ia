from constants import Modes as modes
class Clasicador:
    def __init__(self, responses):
        self.responses = responses
        self.current_mode = modes.NORMAL
        self.modes = modes
    def check_if_math_mode(self, prompt):
        math_keywords = ["matematica", "suma", "resta", "multiplica", "divide", "+", "-", "*", "/","calcula","resultado","cuánto es","cuanto es","calcular"]
        return any(keyword in prompt for keyword in math_keywords)
    def check_if_personal_mode(self, prompt):
        personal_keywords = ["nombre", "edad", "dirección", "teléfono", "correo", "cumpleaños"]
        return any(keyword in prompt for keyword in personal_keywords)
    def check_if_tictactoe_mode(self, prompt):
        tictactoe_keywords = ["tic tac toe","tictactoe", "tres en raya", "jugar"]
        return any(keyword in prompt for keyword in tictactoe_keywords)
    def check_if_test_turning_mode(self, prompt):
        test_keywords = ["test", "prueba", "exam"]
        return any(keyword in prompt for keyword in test_keywords)
    def classify(self, prompt):
        if self.check_if_math_mode(prompt):
            self.current_mode = modes.MATEMATICAS
        elif self.check_if_personal_mode(prompt):
            self.current_mode = modes.PERSONAL
        elif self.check_if_tictactoe_mode(prompt):
            self.current_mode = modes.TICTACTOE
        else:
            self.current_mode = modes.NORMAL
        return self.current_mode


