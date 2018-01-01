import numpy

starting_value = 20151125
current_x = 0
current_y = 0
max_x = 0
max_y = 0
target_x = 3083
target_y = 2978

grid = numpy.zeros((max(target_x * 2, target_y * 2), max(target_x * 2, target_y * 2)))

while current_y < max(target_x * 2, target_y * 2) and current_x < max(target_x * 2, target_y * 2):
    new_value = (starting_value * 252533) % 33554393
    grid[current_y][current_x] = starting_value
    if current_x == max_x:
        max_y += 1
        max_x += 1
        current_y = max_y
        current_x = 0
    else:
        if current_y > 0 and current_x <= max_x:
            current_y -= 1
            current_x += 1
    starting_value = new_value

print int(grid[target_y - 1][target_x - 1])
