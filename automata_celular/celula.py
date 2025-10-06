class Celula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

    def set_alive(self, alive):
        self.alive = alive

    def is_alive(self):
        return self.alive
