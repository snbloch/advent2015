import io
import json
cumulative_sum = 0

file = open('input.txt', 'r')
json_input = json.load(file)
integer_values = []

def find_children(input):
    global integer_values
    if type(input) == dict:
        if 'red' in input.values():
            pass
        else:
            for key, value in input.iteritems():
                if type(value) == int:
                    integer_values.append(value)
                elif type(value) == list:
                    find_children(value)
                elif type(value) == dict:
                    find_children(value)
    elif type(input) == list:
        for value in input:
            find_children(value)
    elif type(input) == int:
        integer_values.append(input)
    return

for key, value in json_input.iteritems():
    find_children(value)

for i in integer_values:
    cumulative_sum += i

print cumulative_sum
