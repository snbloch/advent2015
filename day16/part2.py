import io

attributes = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']
sues = {}
solution = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

file = open('input.txt', 'r')
for line in file:
    line = line.replace(':', '').replace(',', '')
    line = line.strip().split(' ')
    number = int(line[1])
    current_sue = {}
    for attribute in attributes:
        if line[2] == attribute:
            current_sue[attribute] = int(line[3])
        elif line[4] == attribute:
            current_sue[attribute] = int(line[5])
        elif line[6] == attribute:
            current_sue[attribute] = int(line[7])
    sues[number] = current_sue

for key, value in sues.iteritems():
    match_count = 0
    for attribute in value:
        if attribute == 'cats' or attribute == 'trees':
            if value[attribute] > solution[attribute]:
                match_count += 1
        elif attribute == 'pomeranians' or attribute == 'goldfish':
            if value[attribute] < solution[attribute]:
                match_count += 1
        else:
            if value[attribute] == solution[attribute]:
                match_count += 1
    if match_count == 3:
        print key, value
