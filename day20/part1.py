presents_target = 36000000

found = False

house_counter = 1
while found == False:
    num_presents = 0
    elf_counter = 1
    while elf_counter <= house_counter:
        if elf_counter == 1 or house_counter % elf_counter == 0:
            num_presents += elf_counter * 10
        if num_presents >= presents_target:
            print 'Target reached at house number', house_counter
            found = True
        elf_counter += 1
    if house_counter % 10000 == 0:
        print 'Delivered ', num_presents, 'to house ', house_counter
    house_counter += 1
