import io
from collections import Counter

strings = []
nice_count = 0
naughty_count = 0

file = open('input.txt', 'r')
for line in file:
    strings.append(line.strip())

for string in strings:
    pairs = {}
    duplicate_pairs = {}
    repeat_condition = False
    alternate_condition = False
    position = 0
    while position < len(string) - 2:
        if string[position] == string[position + 2]:
            alternate_condition = True
        position += 1
    position = 0
    while position < len(string) - 2:
        pairs[position] = string[position] + string[position + 1]
        position += 1
    for i in pairs.itervalues():
        if string.count(i) > 1:
            repeat_condition = True
            if i[0] == i[1]:
                if string.count(i[0] * 3) == 1 and string.count(i[0] * 4) == 0:
                    repeat_condition = False
    if repeat_condition == True and alternate_condition == True:
        nice_count += 1
    else:
        naughty_count += 1

print 'Nice count: ', nice_count
print 'Naughty count: ', naughty_count
