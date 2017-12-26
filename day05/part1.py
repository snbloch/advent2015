import io

strings = []
nice_count = 0
naughty_count = 0
vowels = 'aeiou'
bad_strings = ['ab', 'cd', 'pq', 'xy']

file = open('input.txt', 'r')
for line in file:
    strings.append(line.strip())

for string in strings:
    vowel_condition = False
    repeat_condition = False
    bad_string_found = False
    position = 0
    vowel_counter = 0
    while position < len(string):
        if string[position] in vowels:
            vowel_counter += 1
        position += 1
    if vowel_counter >= 3:
        vowel_condition = True
    position = 0
    while position < len(string) - 1:
        if string[position] == string[position + 1]:
            repeat_condition = True
        position += 1
    for i in bad_strings:
        if i in string:
            bad_string_found = True
    if vowel_condition == True and repeat_condition == True and bad_string_found == False:
        nice_count += 1
    else:
        naughty_count += 1

print 'Nice count: ', nice_count
print 'Naughty count: ', naughty_count
