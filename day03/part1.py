import io
import numpy

moves = []

file = open('input.txt', 'r')
for line in file:
    for move in line.strip():
        moves.append(move)

length = len(moves)
grid = numpy.zeros((length, length))

cur_x = length / 2
cur_y = length / 2
grid[cur_y][cur_x] += 1
for move in moves:
    if move == '^':
        cur_y -= 1
    elif move == '>':
        cur_x += 1
    elif move == 'v':
        cur_y += 1
    elif move == '<':
        cur_x -= 1
    grid[cur_y][cur_x] += 1

houses_delivered = numpy.count_nonzero(grid)

print houses_delivered
