import io
from itertools import combinations

containers = []
target = 150
combination_counter = 0

file = open('input.txt', 'r')
for line in file:
    containers.append(int(line.strip()))

num_containers = len(containers)
counter = 1
while counter <= num_containers:
    capacity = [combination for combination in combinations(containers, counter)]
    for i in capacity:
        current_capacity = 0
        for j in i:
            current_capacity += j
        if current_capacity == 150:
            combination_counter += 1
    counter += 1

print combination_counter
