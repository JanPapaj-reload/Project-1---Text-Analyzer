def chess_board(size):
    sym = ['#', ' ']
    desk = []

    for row in range(size):
        line = []
        for cell in range(size):
            i = ((cell + row) % 2 == 0)
            line.append(sym[i])
        desk.append(''.join(line))

    print('\n'.join(desk))


chess_board(13)
