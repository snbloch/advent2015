import io

total = 0

file = open('input.txt', 'r')
for line in file:
    l = int(line.strip().split('x')[0])
    w = int(line.strip().split('x')[1])
    h = int(line.strip().split('x')[2])
    bow = l*w*h
    ribbon = min(l*2 + w*2, w*2 + h*2, h*2 + l*2)
    total += ribbon + bow

print total
