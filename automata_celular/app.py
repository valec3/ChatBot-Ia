from tkinter import Tk, Label, Button, ttk, Canvas
# import tkinter as tk
# simple app tkinter

class FluidoGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("Juego de la vida")
        self.window.geometry("700x700")
        self.rows = 10
        self.cols = 10
        self.cell_size = 40
        self.table = [
            [0,1,0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0,1,0],
            [1,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1,0,0,0],
            [0,0,2,2,2,2,0,0,1,0],
            [1,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0,1,0],
        ] # 0:Vacio, 1:Agua , 2:Bloque
        self.canvas = Canvas(self.window, width=self.cols*self.cell_size, 
                                height=self.rows*self.cell_size, bg="white")
        self.canvas.pack()
    def run(self):
        self.paint_grid()
        btn_next = Button(self.window, text="Siguiente Generación", command=self.next_generation)
        btn_next.pack()
        # while True:
        #     self.next_generation()
        #     self.window.update_idletasks()
        #     self.window.update()
        #     self.window.after(1000) #espera 1S

        self.window.mainloop()
    def paint_grid(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "blue" if self.table[i][j] == 1 else "brown" if self.table[i][j] == 2 else "grey20"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")
    def check_is_last_row(self, row):
        return row == self.rows - 1
    def check_next_row_is_empty(self, row, col):
        if row + 1 < self.rows:
            return self.table[row + 1][col] == 0
        return False
    def check_next_row_is_block_and_around_empty(self, row, col):
        if row + 1 < self.rows:
            if self.table[row + 1][col] == 2: # Bloque abajo
                # Verificar si los lados están vacíos
                left_empty = (col - 1 >= 0 and self.table[row][col - 1] == 0)
                right_empty = (col + 1 < self.cols and self.table[row][col + 1] == 0)
                return left_empty or right_empty
        return False
    def check_next_row_is_water(self, row, col):
        if row + 1 < self.rows:
            return self.table[row + 1][col] == 1
        return False
    def check_left_is_empty(self, row, col):
        if col - 1 >= 0:
            return self.table[row][col - 1] == 0
        return False
    def check_right_is_empty(self, row, col):
        if col + 1 < self.cols:
            return self.table[row][col + 1] == 0
        return False
    def next_generation(self):
        new_table = [[0]*self.cols for _ in range(self.rows)]
        last_index = self.rows - 1
        for i in range(last_index, -1, -1):
            for j in range(self.cols):
                if self.table[i][j] == 2: # Bloque
                    new_table[i][j] = 2
                    print("BLOQUE")
                elif self.table[i][j] == 1 and not self.check_is_last_row(i): # Agua
                    if self.check_next_row_is_empty(i, j) or self.check_next_row_is_water(i, j):
                        new_table[i + 1][j] = 1 # Mover agua hacia abajo
                        print("ABAJO AGUA")
                    elif self.check_next_row_is_block_and_around_empty(i, j):
                        if j - 1 >= 0 and self.table[i][j - 1] == 0: # Lado izquierdo vacío y dentro de límites
                            new_table[i][j - 1] = 1 # Mover agua a la izquierda
                            print("AGUA IZQUIERDA")
                        elif j + 1 < self.cols and self.table[i][j + 1] == 0: # Lado derecho vacío y dentro de límites
                            new_table[i][j + 1] = 1 # Mover agua a la derecha
                            print("AGUA DERECHA")
                    else:
                        new_table[i][j] = 1 # Quedarse en su lugar
                        print("AGUA QUIETO")
                else:
                    print("VACIO")
                    new_table[i][j] = 0 # Vacio
        self.table = new_table
        self.paint_grid()
if __name__ == "__main__":
    app = FluidoGame()
    app.run() 