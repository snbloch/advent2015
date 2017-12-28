import io
from itertools import permutations

people = set()
table = []
cumulative_happiness = 0

file = open('input.txt', 'r')
for line in file:
    people.add(line.split(' ')[0])
    if line.split(' ')[2] == 'gain':
        value = int(line.split(' ')[3])
    elif line.split(' ')[2] == 'lose':
        value = 0 - int(line.split(' ')[3])
    table.append(((line.strip().split(' ')[0], line.strip().split(' ')[10].replace('.', '')), value))

num_people = len(people)
seating_arrangement = list(permutations(people))
for arr in seating_arrangement:
    happiness = 0
    counter = 0
    while counter < num_people:
        if counter == num_people - 1:
            left = arr[counter]
            right = arr[0]
        else:
            left = arr[counter]
            right = arr[counter + 1]
        for t in table:
            if t[0] == (left, right):
                happiness += t[1]
            elif t[0] == (right, left):
                happiness += t[1]
        counter += 1
    if happiness > cumulative_happiness:
        cumulative_happiness = happiness

print cumulative_happiness
