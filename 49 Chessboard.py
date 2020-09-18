size = int(input("enter the size: "))
sym = ['#', ' ']
desk = []
for r, row in enumerate(range(size)):
    line = []
    for c, cell in enumerate(range(size)):
        line.append(sym[(r + c) % len(sym)])
    desk.append(''.join(line))

print('\n'.join(desk))