import io

reindeer = []
reindeer_states = {}
reindeer_distances = {}
reindeer_points = {}
max_points = 0

file = open('input.txt', 'r')
for line in file:
    l = line.split(' ')
    reindeer.append([l[0], int(l[3]), int(l[6]), int(l[13])])

seconds = 0
for deer in reindeer:
    reindeer_states[deer[0]] = ['running', 0]
    reindeer_distances[deer[0]] = 0
    reindeer_points[deer[0]] = 0

while seconds < 2503:
    for deer in reindeer:
        if reindeer_states[deer[0]][0] == 'running':
            if reindeer_states[deer[0]][1] != 0 and reindeer_states[deer[0]][1] % deer[2] == 0:
                reindeer_states[deer[0]][0] = 'stopped'
                reindeer_states[deer[0]][1] = 1
            else:
                reindeer_states[deer[0]][1] += 1
                reindeer_distances[deer[0]] += deer[1]
        elif reindeer_states[deer[0]][0] == 'stopped':
            if reindeer_states[deer[0]][1] != 0 and reindeer_states[deer[0]][1] % deer[3] == 0:
                reindeer_states[deer[0]][0] = 'running'
                reindeer_states[deer[0]][1] = 1
                reindeer_distances[deer[0]] += deer[1]
            else:
                reindeer_states[deer[0]][1] += 1
    seconds += 1
    furthest_reindeer_names = []
    furthest_reindeer_distance = 0
    for key, value in reindeer_distances.iteritems():
        if value >= furthest_reindeer_distance:
            furthest_reindeer_distance = value
    for deer in reindeer_distances:
        if reindeer_distances[deer] == furthest_reindeer_distance:
            reindeer_points[deer] += 1

for key, value in reindeer_points.iteritems():
    if value > max_points:
        max_points = value

print max_points
