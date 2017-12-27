puzzle_input = '1113122113'

iter_count = 0
while iter_count < 50:
    position = 1
    output = ''
    copies = 1
    while position < len(puzzle_input):
        digit = puzzle_input[position - 1]
        if puzzle_input[position - 1] == puzzle_input[position]:
            copies += 1
            position += 1
        else:
            output += str(copies)
            output += digit
            copies = 1
            position += 1

    digit = puzzle_input[position - 1]
    output += str(copies)
    output += digit
    puzzle_input = output
    print iter_count + 1, len(puzzle_input)
    iter_count += 1
