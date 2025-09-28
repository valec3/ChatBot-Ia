import json
import random

path_file = "db.json"
with open(path_file, "r", encoding="utf-8") as file:
    options_messages = json.load(file)
    options_messages = dict(options_messages)

words = ["hola", "adiós", "nombre", "ayuda", "información", "preguntas", "bien", "gracias", "día", "tarde", "noche", 
         "asistente", "virtual", "mensaje", "ingresa", "puedo", "hacer", "cual", "eres", "quién", "qué", "cómo", 
         "estás", "qué", "puedes", "hacer", "tú", "yo", "nosotros", "ellos", "ellas", "usted", "ustedes", "por favor", 
         "gracias", "de nada", "lo siento", "no entiendo", "reformular", "preguntar", "responder", "información", 
         "ayuda", "asistente", "virtual", "nombre", "día", "tarde", "noche"]

#TODO: uasr modos
modos = {0:"normal", 1:"matemáticas", 2:"personal", 3:"tictactoe"}
keywords_info = ["nombre", "edad", "correo", "telefono", "dirección","cumpleaños"]

def generar_random_response():
    words_elegidas = random.sample(words, 5)
    return " ".join(words_elegidas)

def format_rsp_mat(operation="1+1"):
     print(operation)
     calculo = eval(operation)
     return f"El resultado de {operation} es {calculo}"

def check_contains_math_expression(prompt):
    numbers = set("0123456789")
    math_symbols = set("+-*/(). ")
    pos_promt_check = []
    for char in prompt:
        if char in numbers:
            pos_promt_check.append(1)
        elif char in math_symbols:
            pos_promt_check.append(2)
        else:
            pos_promt_check.append(0)

    for i in range(len(pos_promt_check)-2):
        if pos_promt_check[i] == 1 and pos_promt_check[i+1] in [1,2] and pos_promt_check[i+2] in [1,2]:
            try:
                result = format_rsp_mat(prompt[i:])
                return result
            except Exception as e:
                return "No se pudo calcular la expresión matemática."
    return None

def opcion_cercana(prompt, options):
    prompt = prompt.lower()
    for option in options:
        option_words = option.lower().split()
        prompt_words = prompt.split()
        common_words = set(option_words) & set(prompt_words)
        if len(common_words) >= 1:
            return options[option]
    return generar_random_response()


# JUEGO TRES EN RAYA

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # filas ganadoras
        [0,3,6], [1,4,7], [2,5,8], # columnas
        [0,4,8], [2,4,6]           # diagonales
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def play_tic_tac_toe():
    board = [" "]*9
    user = "X"
    ai = "O"
    turn = "user"

    print("🎮 Empezamos al tres en raya 🎮")
    print_board(board)

    while True:
        if turn == "user":
            # TODO:agregar validacione para evitar error de rango
            move = input("Elige una posición (1-9): ")
            # check int
            if move not in ["0","1","2","3","4","5","6","7","8","9"]:
                print("Asistente: Saliendo del juego de tres en raya.")
                return
            move = int(move) - 1
            if board[move] == " ":
                board[move] = user
                turn = "ai"
            else:
                print("❌ Esa posición ya está ocupada.")
                continue
        else:
            ################33
            move = random.choice([i for i, x in enumerate(board) if x == " "])
            board[move] = ai
            turn = "user"
            print(f"La IA juega en la posición {move+1}")

        print_board(board)

        # Verificar ganador
        if check_winner(board, user):
            print("🎉 ¡Ganaste!")
            break
        elif check_winner(board, ai):
            print("😢 La IA ganó.")
            break
        elif " " not in board:
            print("🤝 Empate.")
            break

def save_user_info_file(data, filename="user_info.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_user_info_file(filename="user_info.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
def check_is_personal_info(prompt):
    for keyword in keywords_info:
        if keyword in prompt.lower():
            return True
    return False
def save_personal_info(prompt):
    response =""
    for keyword in keywords_info:
        options_users = load_user_info_file()
        if keyword in prompt.lower() and keyword in options_users:
            response= f"Tu {keyword} es {options_users[keyword]}. "
            return response
    print("No tengo información personal sobre ti. ¿Quieres proporcionarla?")
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() in ["no", "n"]:
            response = "Entendido. No se guardará ninguna información personal."
            break
        elif user_input.lower() in ["sí", "si", "sis","s"]:
            user_info = {}
            for keyword in keywords_info:
                info = input(f"Por favor, ingresa tu {keyword}: ")
                user_info[keyword] = info
            save_user_info_file(user_info)
            response = "Gracias. Tu información personal ha sido guardada."
            break
        else:
            response = "Por favor, responde con 'sí' o 'no'."
            print("Asistente:", response)
    return response

#
#TODO: Tarea agregar el juego tres en raya en el avance
#
# bucle principall............................................

while True:
    prompt = str(input("Usuario: "))
    response = options_messages.get(prompt, "Lo siento, no entiendo tu mensaje. ¿Podrías reformularlo?")

    if prompt.lower() in ["adiós", "salir", "terminar"]:
        print("Asistente: ¡Hasta luego! Que tengas un buen día.")
        break
    if any(word in prompt.lower() for word in ["tic", "tac","toe","tres en raya","jugar tres en raya"]):
        play_tic_tac_toe()
        continue

    if check_contains_math_expression(prompt):
        response = check_contains_math_expression(prompt)
    elif check_is_personal_info(prompt):
        response = save_personal_info(prompt)

    elif not options_messages.get(prompt):
        response = opcion_cercana(prompt, options_messages)
        options_messages[prompt] = response
        with open(path_file, "w", encoding="utf-8") as file:
            json.dump(options_messages, file, indent=4, ensure_ascii=False)

    print("Asistente:", response)
