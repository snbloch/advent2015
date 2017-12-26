import io

strings = []
literal_characters = 0
memory_characters = 0

file = open('input.txt', 'r')
for line in file:
    strings.append(line.strip())

for string in strings:
    literal_characters += len(string)
    position = 1
    while position < len(string) - 1:
        if string[position] != '\\':
            memory_characters += 1
            position += 1
        else:
            if string[position + 1] == '\\' or string[position + 1] == '"':
                memory_characters += 1
                position += 2
            elif string[position + 1] == 'x':
                memory_characters += 1
                position += 4

print literal_characters - memory_characters
