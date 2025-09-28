import json
import random
from constants import Modes as modes
from tictactoe import TicTacToe
from clasificador import Clasicador
from calculator import Calculator
def load_db_responses():
    with open("db.json", "r", encoding="utf-8") as file:
        json_responses = json.load(file)
        return dict(json_responses)
def load_db_personal_info():
    with open("user_info.json", "r", encoding="utf-8") as file:
        json_personal_info = json.load(file)
        return dict(json_personal_info)
def load_db_words ():
    # TODO: cargar desde archivo JSON
    # with open("words.json", "r", encoding="utf-8") as file:
    #     return json.load(file)
    return ["hola", "adiós", "gracias", "por favor", "sí", "no"]


class ChatBot:
    def __init__(self, name="Asistente"):
        self.name = name
        self.responses = load_db_responses()
        self.keywords_info = ["nombre", "edad", "dirección", "teléfono", "correo", "cumpleaños"]
        self.modes = modes
        self.words = load_db_words()
        self.personal_info = load_db_personal_info()
        self.current_mode = modes.NORMAL
        self.game = None  # Inicialmente no hay juego activo :v
        self.classifier = Clasicador(self.responses)
        self.calculator = Calculator()
    def set_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
            print(5*"-")
            print(f"Cambiando a modo: {mode.value}")
            print(5*"-")
            return f"Modo cambiado a {mode.value}."
            
        else:
            return "Modo no reconocido. Los modos disponibles son: " + ", ".join(self.modes.values())
    def detect_mode(self, prompt):
        if self.classifier.check_if_math_mode(prompt):
            return self.set_mode(modes.MATEMATICAS)
        elif self.classifier.check_if_tictactoe_mode(prompt):
            return self.set_mode(modes.TICTACTOE)
        elif self.classifier.check_if_personal_mode(prompt):
            return self.set_mode(modes.PERSONAL)
        else:
            return self.set_mode(modes.NORMAL)
    def get_input_prompt(self):
        prompt = input("Tú: ")
        self.detect_mode(prompt)
        return prompt.strip().lower()
    def get_response_normal(self, prompt):
        words_prompt = prompt.split()
        # Buscar coincidencias en las opciones
        for option in self.responses:
            option_words = option.lower().split()
            common_words = set(option_words) & set(words_prompt)
            if len(common_words) >= 1:
                return self.responses[option]
        return "No entiendo tu mensaje. ¿Puedes reformularlo?"
    def get_response_math(self, prompt):
        result, success = self.calculator.calculate(prompt)
        if success:
            return f"El resultado es: {result}"
        else:
            return result
    def save_response(self, prompt, response):
        self.responses[prompt] = response
        with open("db.json", "w", encoding="utf-8") as file:
            json.dump(self.responses, file, ensure_ascii=False, indent=4)
    def save_response_personal_info(self, prompt, response):
        self.personal_info[prompt] = response
        with open("user_info.json", "w", encoding="utf-8") as file:
            json.dump(self.personal_info, file, ensure_ascii=False, indent=4)
    def run_tictactoe(self, prompt):
        if self.game is None:
            self.game = TicTacToe()
            return "¡Comencemos una partida de Tres en Raya!\n" + self.game.display_board() + "\nElige una posición del 0 al 8 para hacer tu movimiento."
        else:
            try:
                move = int(prompt)
                if move < 0 or move > 8:
                    return "Por favor, elige una posición válida del 0 al 8."
                response = self.game.player_move(move)
                if "ganado" in response or "empate" in response:
                    self.game = None  # Reiniciar el juego después de que termine
                return response
            except ValueError:
                return "Por favor, ingresa un número del 0 al 8 para hacer tu movimiento."
    def run(self):
        print(f"{self.name} (${self.current_mode}): ¡Hola! Soy tu asistente. ¿En qué puedo ayudarte hoy?")
        while True:
            prompt = self.get_input_prompt()
            if prompt in ["salir", "exit", "quit"]:
                print(f"{self.name}: ¡Hasta luego!")
                break
            if self.current_mode == modes.NORMAL:
                response = self.get_response_normal(prompt)
            elif self.current_mode == modes.MATEMATICAS:
                response = self.get_response_math(prompt)
            elif self.current_mode == modes.PERSONAL:
                response = self.handle_personal_info(prompt)
            elif self.current_mode == modes.TICTACTOE:
                response = self.run_tictactoe(prompt)
            else:
                response = "Modo no soportado actualmente."
            print(f"{self.name} ({self.current_mode.value}): {response}")


# TEST

if __name__ == "__main__":
    bot = ChatBot()
    bot.run()