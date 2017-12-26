import io
import numpy
instructions = []
starts = []
ends = []

file = open('input.txt', 'r')
for line in file:
    if 'turn on' in line:
        instructions.append('turn on')
        line = line.replace('turn on ', '')
    elif 'turn off' in line:
        instructions.append('turn off')
        line = line.replace('turn off ', '')
    elif 'toggle' in line:
        instructions.append('toggle')
        line = line.replace('toggle ', '')
    starts.append(list(line.split(' through ')[0].strip().split(',')))
    ends.append(list(line.split(' through ')[1].strip().split(',')))

for i in starts:
    i[0] = int(i[0])
    i[1] = int(i[1])
for i in ends:
    i[0] = int(i[0])
    i[1] = int(i[1])

height = 1000
width = 1000
grid = numpy.zeros((height, width))

counter = 0
while counter < len(instructions):
    if instructions[counter] == 'turn on':
        cur_y = starts[counter][1]
        while cur_y <= ends[counter][1]:
            cur_x = starts[counter][0]
            while cur_x <= ends[counter][0]:
                grid[cur_y][cur_x] = 1
                cur_x += 1
            cur_y += 1
    if instructions[counter] == 'turn off':
        cur_y = starts[counter][1]
        while cur_y <= ends[counter][1]:
            cur_x = starts[counter][0]
            while cur_x <= ends[counter][0]:
                grid[cur_y][cur_x] = 0
                cur_x += 1
            cur_y += 1
    if instructions[counter] == 'toggle':
        cur_y = starts[counter][1]
        while cur_y <= ends[counter][1]:
            cur_x = starts[counter][0]
            while cur_x <= ends[counter][0]:
                if grid[cur_y][cur_x] == 0:
                    grid[cur_y][cur_x] = 1
                elif grid[cur_y][cur_x] == 1:
                    grid[cur_y][cur_x] = 0
                cur_x += 1
            cur_y += 1
    counter += 1

print numpy.count_nonzero(grid)
