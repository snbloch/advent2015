import io

strings = []
literal_characters = 0
encoded_characters = 0

file = open('input.txt', 'r')
for line in file:
    strings.append(line.strip())

for string in strings:
    # Seed encode_counter with starting and ending quotes
    encode_counter = 2
    literal_characters += len(string)
    position = 0
    while position < len(string):
        if string[position] == '"':
            encode_counter += 2
            position += 1
        elif string[position] == '\\':
            encode_counter += 2
            position += 1
        else:
            encode_counter += 1
            position += 1
    encoded_characters += encode_counter

print encoded_characters - literal_characters
