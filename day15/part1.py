import io

ingredients = {}
high_score = 0

file = open('input.txt', 'r')
for line in file:
    line = line.strip().split(' ')
    ingredients[line[0].replace(':', '')] = [int(line[2].replace(',', '')), int(line[4].replace(',', '')), int(line[6].replace(',', '')), int(line[8].replace(',', '')), int(line[10].replace(',', ''))]

num_frosting = 0
while num_frosting <= 100:
    num_candy = 0
    while num_candy <= 100:
        num_butterscotch = 0
        while num_butterscotch <= 100:
            num_sugar = 0
            while num_sugar <= 100:
                if num_frosting + num_candy + num_butterscotch + num_sugar == 100:
                    capacity = num_frosting * ingredients['Frosting'][0] + num_candy * ingredients['Candy'][0] + num_butterscotch * ingredients['Butterscotch'][0] + num_sugar * ingredients['Sugar'][0]
                    durability = num_frosting * ingredients['Frosting'][1] + num_candy * ingredients['Candy'][1] + num_butterscotch * ingredients['Butterscotch'][1] + num_sugar * ingredients['Sugar'][1]
                    flavor = num_frosting * ingredients['Frosting'][2] + num_candy * ingredients['Candy'][2] + num_butterscotch * ingredients['Butterscotch'][2] + num_sugar * ingredients['Sugar'][2]
                    texture = num_frosting * ingredients['Frosting'][3] + num_candy * ingredients['Candy'][3] + num_butterscotch * ingredients['Butterscotch'][3] + num_sugar * ingredients['Sugar'][3]
                    if capacity < 0:
                        capacity = 0
                    if durability < 0:
                        durability = 0
                    if flavor < 0:
                        flavor = 0
                    if texture < 0:
                        texture = 0
                    score = capacity * durability * flavor * texture
                    if score > high_score:
                        high_score = score
                num_sugar += 1
            num_butterscotch += 1
        num_candy += 1
    num_frosting += 1

print high_score
