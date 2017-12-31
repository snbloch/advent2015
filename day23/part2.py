import io

instructions = []

file = open('input.txt', 'r')
for line in file:
    line = line.strip().split(',')
    if len(line) == 1:
        instructions.append([line[0].split(' ')[0].strip(), line[0].split(' ')[1].strip()])
    else:
        instructions.append([line[0].split(' ')[0].strip(), line[0].split(' ')[1].strip(), line[1].strip()])

reg_a = 1
reg_b = 0
position = 0
while position >= 0 and position < len(instructions):
    if instructions[position][0] == 'hlf':
        if instructions[position][1] == 'a':
            reg_a /= 2
        elif instructions[position][1] == 'b':
            reg_b /= 2
        position += 1
    elif instructions[position][0] == 'tpl':
        if instructions[position][1] == 'a':
            reg_a *= 3
        elif instructions[position][1] == 'b':
            reg_b *= 3
        position += 1
    elif instructions[position][0] == 'inc':
        if instructions[position][1] == 'a':
            reg_a += 1
        elif instructions[position][1] == 'b':
            reg_b += 1
        position += 1
    elif instructions[position][0] == 'jmp':
        if instructions[position][1][0] == '+':
            position += int(instructions[position][1][1:])
        elif instructions[position][1][0] == '-':
            position -= int(instructions[position][1][1:])
    elif instructions[position][0] == 'jie':
        if instructions[position][1] == 'a':
            if reg_a % 2 == 0:
                if instructions[position][2][0] == '+':
                    position += int(instructions[position][2][1:])
                elif instructions[position][2][0] == '-':
                    position -= int(instructions[position][2][1:])
            else:
                position += 1
        elif instructions[position][1] == 'b':
            if reg_b % 2 == 0:
                if instructions[position][2][0] == '+':
                    position += int(instructions[position][2][1:])
                elif instructions[position][2][0] == '-':
                    position -= int(instructions[position][2][1:])
            else:
                position += 1
    elif instructions[position][0] == 'jio':
        if instructions[position][1] == 'a':
            if reg_a == 1:
                if instructions[position][2][0] == '+':
                    position += int(instructions[position][2][1:])
                elif instructions[position][2][0] == '-':
                    position -= int(instructions[position][2][1:])
            else:
                position += 1
        elif instructions[position][1] == 'b':
            if reg_b == 1:
                if instructions[position][2][0] == '+':
                    position += int(instructions[position][2][1:])
                elif instructions[position][2][0] == '-':
                    position -= int(instructions[position][2][1:])
            else:
                position += 1

print reg_b
