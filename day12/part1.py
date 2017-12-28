import io
cumulative_sum = 0

file = open('input.txt', 'r')
json_input = file.read()
values = []

json_input = json_input.strip().replace('{', '').replace('}', '').replace('[', '').replace(']', '').split(':')
for i in json_input:
    values.append(i.split(','))

for i in values:
    for j in i:
        if j[0] == '"':
            pass
        else:
            cumulative_sum += int(j)

print cumulative_sum
