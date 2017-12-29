import io
import numpy
initial_state = []

file = open('input.txt', 'r')
for line in file:
    initial_state.append(line.strip())

height = 100
width = 100
grid = numpy.zeros((height, width))
y_counter = 0
while y_counter < height:
    x_counter = 0
    while x_counter < width:
        if initial_state[y_counter][x_counter] == '#':
            grid[y_counter][x_counter] = 1
        x_counter += 1
    y_counter += 1

iter_counter = 0
while iter_counter < 100:
    grid[0][0] = 1
    grid[0][width - 1] = 1
    grid[height - 1][0] = 1
    grid[height - 1][width - 1] = 1
    temp_grid = numpy.empty((height, width))
    y_counter = 0
    while y_counter < height:
        x_counter = 0
        while x_counter < width:
            num_neighbors_on = 0
            if x_counter == 0 and y_counter == 0:
                neighbors = [(0,1), (1,1), (1,0)]
            elif x_counter == width - 1 and y_counter == height - 1:
                neighbors = [(height - 2, width - 2), (height - 2, width - 1), (height - 1, width - 2)]
            elif x_counter == 0 and y_counter == height - 1:
                neighbors = [(height - 2, 0), (height - 2, 1), (height - 1, 1)]
            elif x_counter == width - 1 and y_counter == 0:
                neighbors = [(0, width - 2), (1, width - 2), (1, width - 1)]
            elif x_counter == 0:
                neighbors = [(y_counter - 1, 0), (y_counter - 1, 1), (y_counter, 1), (y_counter + 1, 1), (y_counter + 1, 0)]
            elif x_counter == width - 1:
                neighbors = [(y_counter - 1, width - 1), (y_counter - 1, width - 2), (y_counter, width - 2), (y_counter + 1, width - 2), (y_counter + 1, width - 1)]
            elif y_counter == 0:
                neighbors = [(0, x_counter - 1), (1, x_counter - 1), (1, x_counter), (1, x_counter + 1), (0, x_counter + 1)]
            elif y_counter == height - 1:
                neighbors = [(height - 1, x_counter - 1), (height - 2, x_counter - 1), (height - 2, x_counter), (height - 2, x_counter + 1), (height - 1, x_counter + 1)]
            else:
                neighbors = [(y_counter - 1, x_counter - 1), (y_counter - 1, x_counter), (y_counter - 1, x_counter + 1), (y_counter, x_counter + 1), (y_counter + 1, x_counter + 1), (y_counter + 1, x_counter), (y_counter + 1, x_counter - 1), (y_counter, x_counter - 1)]
            for i in neighbors:
                if grid[i[0]][i[1]] == 1:
                    num_neighbors_on += 1
            if grid[y_counter][x_counter] == 1:
                if num_neighbors_on == 2 or num_neighbors_on == 3:
                    temp_grid[y_counter][x_counter] = 1
                else:
                    temp_grid[y_counter][x_counter] = 0
            elif grid[y_counter][x_counter] == 0:
                if num_neighbors_on == 3:
                    temp_grid[y_counter][x_counter] = 1
                else:
                    temp_grid[y_counter][x_counter] = 0
            x_counter += 1
        y_counter += 1
    grid = temp_grid
    grid[0][0] = 1
    grid[0][width - 1] = 1
    grid[height - 1][0] = 1
    grid[height - 1][width - 1] = 1
    iter_counter += 1

print numpy.count_nonzero(grid)
