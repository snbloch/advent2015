presents_target = 36000000

found = False

house_counter = 1
while found == False:
    houses_visited = {}
    num_presents = 0
    elf_counter = 1
    while elf_counter <= house_counter:
        if houses_visited.get(elf_counter) == None:
            houses_visited[elf_counter] = 0
        if (elf_counter == 1 or house_counter % elf_counter == 0) and houses_visited[elf_counter] < 50:
            num_presents += elf_counter * 11
            houses_visited[elf_counter] += 1
        if num_presents >= presents_target:
            print 'Target reached at house number', house_counter
            found = True
        elf_counter += 1
    if house_counter % 10000 == 0:
        print 'Delivered ', num_presents, 'to house ', house_counter
    house_counter += 1
