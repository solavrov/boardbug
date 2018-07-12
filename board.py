from bug import Bug
from fun import get_frame


class Board:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.empty = 0
        self.poop = 1
        self.board = get_frame(n, m, self.empty, self.poop)
        self.bug = Bug()
        self.show_bug()

    def show_bug(self):
        self.board[self.bug.y][self.bug.x] = self.bug.sign

    def poop_bug(self):
        self.board[self.bug.y][self.bug.x] = self.poop

    def __str__(self):
        s = ''
        for e in self.board:
            s += str(e) + '\n'
        return s

    def move_bug(self) -> bool:
        self.poop_bug()
        turn_number = 0
        while turn_number < 4:
            self.bug.move()
            if self.board[self.bug.y][self.bug.x] == self.poop:
                self.bug.move_back()
                self.bug.turn()
                turn_number += 1
            else:
                break
        self.show_bug()
        return turn_number < 4
