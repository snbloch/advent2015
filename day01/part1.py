import io

current_floor = 0
moves = []

file = open('input.txt', 'r')
for line in file:
    for move in line.strip():
        moves.append(move)

for i in moves:
    if i == '(':
        current_floor += 1
    elif i == ')':
        current_floor -= 1

print current_floor
