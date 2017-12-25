import io

total = 0

file = open('input.txt', 'r')
for line in file:
    l = int(line.strip().split('x')[0])
    w = int(line.strip().split('x')[1])
    h = int(line.strip().split('x')[2])
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    total += area + slack

print total
