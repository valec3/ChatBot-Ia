class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Un tablero de 3x3 representado como una lista
        self.current_winner = None  # Mantener el registro del ganador!
    def display_board(self):
        # Mostrar el tablero
        board_lines = []
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            board_lines.append('| ' + ' | '.join(row) + ' |')
        return '\n'.join(board_lines)
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        # Revisar las filas, columnas y diagonales para un ganador
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
    def player_move(self, move):
        if self.make_move(move, 'X'):
            if self.current_winner:
                return "¡Felicidades! Has ganado!\n" + self.display_board()
            elif not self.empty_squares():
                return "Es un empate!\n" + self.display_board()
            else:
                computer_move = self.computer_move()
                if self.current_winner:
                    return "La computadora ha ganado!\n" + self.display_board()
                elif not self.empty_squares():
                    return "Es un empate!\n" + self.display_board()
                else:
                    return "Tu movimiento:\n" + self.display_board() + "\nTurno de la computadora."
        else:
            return "Movimiento inválido. Intenta de nuevo."
    def computer_move(self):
        square = self.get_best_move()
        self.make_move(square, 'O')
        return square
    def get_best_move(self):
        if len(self.available_moves()) == 9:
            square = 4  # Elegir el centro si está disponible
        else:
            square = self.minimax('O')['position']
        return square
    def minimax(self, player):
        max_player = 'O'  # La computadora es el jugador máximo
        other_player = 'X' if player == 'O' else 'O'
        if self.current_winner == other_player:
            return {'position': None, 'score': 1 * (self.num_empty_squares() + 1) if other_player == max_player else -1 * (self.num_empty_squares() + 1)}
        elif not self.empty_squares():
            return {'position': None, 'score': 0}
        if player == max_player:
            best = {'position': None, 'score': -float('inf')}
        else:
            best = {'position': None, 'score': float('inf')}
        for possible_move in self.available_moves():
            self.make_move(possible_move, player)
            sim_score = self.minimax(other_player)
            self.board[possible_move] = ' '
            self.current_winner = None
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
