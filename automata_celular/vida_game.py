from tkinter import Tk, Label, Button, ttk, Canvas
# import tkinter as tk
# simple app tkinter

class VidaGame:
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
            [1,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0,1,0],
            [1,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0,1,0],
        ]
        self.canvas = Canvas(self.window, width=self.cols*self.cell_size, 
                                height=self.rows*self.cell_size, bg="white")
        self.canvas.pack()
    def run(self):
        self.paint_grid()
        # btn_next = Button(self.window, text="Siguiente Generación", command=self.next_generation)
        # btn_next.pack()
        while True:
            self.next_generation()
            self.window.update_idletasks()
            self.window.update()
            self.window.after(1000) #espera 1S

        self.window.mainloop()
    def paint_grid(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "red" if self.table[i][j] == 1 else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")
    def count_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions: #dr: delta row, dc: delta col
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.table[r][c]
        return count
    def next_generation(self):
        new_table = [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if self.table[i][j] == 1: #celula viva
                    if neighbors < 2 or neighbors > 3:
                        new_table[i][j] = 0 #muere
                    else:
                        new_table[i][j] = 1 #sobrevive
                else: #celula muerta
                    if neighbors == 3:
                        new_table[i][j] = 1 #nace
                print(f"Cell ({i},{j}) neighbors: {neighbors} -> {new_table[i][j]}")
        self.table = new_table
        self.paint_grid()
if __name__ == "__main__":
    app = VidaGame()
    app.run() 