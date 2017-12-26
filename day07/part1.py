import io

operators = ['AND', 'OR', 'NOT', 'RSHIFT', 'LSHIFT']
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
source = []
destination = []
wires = {}

file = open('input.txt', 'r')
for line in file:
    source.append(line.strip().split(' -> ')[0])
    destination.append(line.strip().split(' -> ')[1])

def retrieve_value(wire):
    bitwise_source = False
    if wires.get(wire) != None:
        return int(wires[wire])
    else:
        index = destination.index(wire)
        for i in operators:
            if i in source[index]:
                bitwise_source = True
                return bitwise_operation(source[index])
        if bitwise_source == False:
            if str(source[index])[0] in alpha:
                return int(retrieve_value(source[index]))
            else:
                return int(source[index])

def bitwise_operation(counter):
    global wires
    if 'AND' in source[source.index(counter)]:
        left = source[source.index(counter)].split(' AND ')[0]
        right = source[source.index(counter)].split(' AND ')[1]
        if wires.get(left) == None:
            if str(left)[0] not in alpha:
                left = int(left)
            else:
                left = int(retrieve_value(left))
        else:
            left = int(wires[left])
        if wires.get(right) == None:
            if str(right)[0] not in alpha:
                right = int(right)
            else:
                right = int(retrieve_value(right))
        else:
            right = int(wires[right])
        wires[destination[source.index(counter)]] = left & right
        return wires[destination[source.index(counter)]]
    elif 'OR' in source[source.index(counter)]:
        left = source[source.index(counter)].split(' OR ')[0]
        right = source[source.index(counter)].split(' OR ')[1]
        if wires.get(left) == None:
            if str(left)[0] not in alpha:
                left = int(left)
            else:
                left = int(retrieve_value(left))
        else:
            left = int(wires[left])
        if wires.get(right) == None:
            if str(right)[0] not in alpha:
                right = int(right)
            else:
                right = int(retrieve_value(right))
        else:
            right = int(wires[right])
        wires[destination[source.index(counter)]] = left | right
        return wires[destination[source.index(counter)]]
    elif 'NOT' in source[source.index(counter)]:
        left = source[source.index(counter)].split('NOT ')[1]
        if wires.get(left) == None:
            if str(left)[0] not in alpha:
                left = int(left)
            else:
                left = int(retrieve_value(left))
        else:
            left = int(wires[left])
        wires[destination[source.index(counter)]] = ~ left
        return wires[destination[source.index(counter)]]
    elif 'RSHIFT' in source[source.index(counter)]:
        left = source[source.index(counter)].split(' RSHIFT ')[0]
        right = int(source[source.index(counter)].split(' RSHIFT ')[1])
        if wires.get(left) == None:
            if str(left)[0] not in alpha:
                left = int(left)
            else:
                left = int(retrieve_value(left))
        else:
            left = int(wires[left])
        wires[destination[source.index(counter)]] = left >> right
        return wires[destination[source.index(counter)]]
    elif 'LSHIFT' in source[source.index(counter)]:
        left = source[source.index(counter)].split(' LSHIFT ')[0]
        right = int(source[source.index(counter)].split(' LSHIFT ')[1])
        if wires.get(left) == None:
            if str(left)[0] not in alpha:
                left = int(left)
            else:
                left = int(retrieve_value(left))
        else:
            left = int(wires[left])
        wires[destination[source.index(counter)]] = left << right
        return wires[destination[source.index(counter)]]
    else:
        left = source[counter]
        if str(left)[0] in alpha:
            if wires.get(left) != None:
                wires[destination[counter]] = int(wires.get(left))
                return wires[destination[counter]]
            else:
                wires[destination[counter]] = int(retrieve_value(left))
                return wires[destination[counter]]
        else:
            wires[destination[counter]] = int(left)
            return wires[destination[counter]]

print retrieve_value('a')
