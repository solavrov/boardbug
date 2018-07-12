class Bug:

    def __init__(self, x=1, y=1, vx=1, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.sign = 8

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def move_back(self):
        self.x -= self.vx
        self.y -= self.vy

    # to mention: if vs elif
    def turn(self):
        if self.vx == 1 and self.vy == 0:
            self.vx = 0
            self.vy = 1
        elif self.vx == 0 and self.vy == 1:
            self.vx = -1
            self.vy = 0
        elif self.vx == -1 and self.vy == 0:
            self.vx = 0
            self.vy = -1
        elif self.vx == 0 and self.vy == -1:
            self.vx = 1
            self.vy = 0

    def print_pos(self):
        print('x =', self.x, ' y =', self.y)
