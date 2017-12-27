puzzle_input = 'cqjxjnds'
rotation_count = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'
bad_letters_list = 'iol'
doubles = []
for i in alpha:
    doubles.append(i * 2)

def increment_letter(letter):
    cur_letter_index = alpha.index(letter)
    if cur_letter_index == 25:
        new_letter = alpha[0]
        wrapped = True
    else:
        new_letter = alpha[cur_letter_index + 1]
        wrapped = False
    return new_letter, wrapped

def increment_password(password):
    new_password = []
    wrapped = False
    position = len(password) - 1
    new_letter, wrapped = increment_letter(password[position])
    new_password = [new_letter] + new_password
    while wrapped == True:
        if position == 0:
            position = len(password) - 1
        else:
            position -= 1
        new_letter, wrapped = increment_letter(password[position])
        new_password = [new_letter] + new_password
    if position == 0:
        position = len(password) - 1
    else:
        position -= 1
    while position >= 0:
        new_password = [password[position]] + new_password
        position -= 1
    new_password_string = ''
    for i in new_password:
        new_password_string += i
    return new_password_string

while rotation_count < 2:
    good_password = False
    while good_password == False:
        password = increment_password(puzzle_input)
        straight = False
        bad_letters = False
        pairs = False
        position = 0
        while position < len(alpha) - 2:
            if alpha[position:position + 3] in password:
                straight = True
            position += 1
        if straight == False:
            puzzle_input = password
            continue
        position = 0
        while position < len(bad_letters_list):
            if bad_letters_list[position] in password:
                bad_letters = True
            position += 1
        if bad_letters == True:
            puzzle_input = password
            continue
        position = 0
        pair_count = 0
        while position < len(doubles):
            if doubles[position] in password:
                pair_count += 1
            position += 1
        if pair_count >= 2:
            pairs = True
        if pairs == False:
            puzzle_input = password
            continue
        else:
            puzzle_input = password
            good_password = True
            rotation_count += 1

print password
