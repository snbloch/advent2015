import io

current_floor = 0
moves = []

file = open('input.txt', 'r')
for line in file:
    for move in line.strip():
        moves.append(move)

counter = 0
for i in moves:
    if i == '(':
        current_floor += 1
    elif i == ')':
        current_floor -= 1
    counter += 1
    if current_floor == -1:
        print counter
        break
