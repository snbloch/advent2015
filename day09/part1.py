import io
from itertools import permutations

legs = []
cities = set([])
min_distance = None
seen_routes = []

file = open('input.txt', 'r')
for line in file:
    distance = int(line.strip().split(' = ')[1])
    source = line.strip().split(' = ')[0].split(' to ')[0]
    dest = line.strip().split(' = ')[0].split(' to ')[1]
    legs.append(((source, dest), distance))

for city in legs:
    cities.add(city[0][0])
    cities.add(city[0][1])

for route in list(permutations(cities)):
    seen_routes.append(route)

for route in seen_routes:
    route_distance = 0
    count = 0
    while count < len(route) - 1:
        leg_origin = route[count]
        leg_destination = route[count + 1]
        for leg in legs:
            if leg[0] == (leg_origin, leg_destination):
                route_distance += leg[1]
            elif leg[0] == (leg_destination, leg_origin):
                route_distance += leg[1]
        count += 1
    if min_distance == None:
        min_distance = route_distance
    elif route_distance < min_distance:
        min_distance = route_distance

print min_distance
