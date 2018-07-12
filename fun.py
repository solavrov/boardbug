# to mention: copy list b=list(a)
def get_frame(n, m, empty_sign, border_sign):
    board = []
    line1 = [border_sign] * (n + 2)
    line2 = [empty_sign] * (n + 2)
    line2[0] = line2[n + 1] = border_sign
    board.append(list(line1))
    for i in range(m):
        board.append(list(line2))
    board.append(list(line1))
    return board

