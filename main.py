from board import Board

b = Board(10, 10)
print(b)

while b.move_bug():
    print(b)

b.bug.print_pos()
