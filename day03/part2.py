import io
import numpy

moves = []

file = open('input.txt', 'r')
for line in file:
    for move in line.strip():
        moves.append(move)

length = len(moves)
grid = numpy.zeros((length, length))

santa_x = length / 2
santa_y = length / 2
robosanta_x = length / 2
robosanta_y = length / 2
grid[santa_y][santa_x] += 1
grid[robosanta_y][robosanta_x] += 1

move_counter = 2
for move in moves:
    if move == '^':
        if move_counter % 2 == 0:
            santa_y -= 1
            grid[santa_y][santa_x] += 1
        else:
            robosanta_y -= 1
            grid[robosanta_y][robosanta_x] += 1
    elif move == '>':
        if move_counter % 2 == 0:
            santa_x += 1
            grid[santa_y][santa_x] += 1
        else:
            robosanta_x += 1
            grid[robosanta_y][robosanta_x] += 1
    elif move == 'v':
        if move_counter % 2 == 0:
            santa_y += 1
            grid[santa_y][santa_x] += 1
        else:
            robosanta_y += 1
            grid[robosanta_y][robosanta_x] += 1
    elif move == '<':
        if move_counter % 2 == 0:
            santa_x -= 1
            grid[santa_y][santa_x] += 1
        else:
            robosanta_x -= 1
            grid[robosanta_y][robosanta_x] += 1
    move_counter += 1

houses_delivered = numpy.count_nonzero(grid)

print houses_delivered
