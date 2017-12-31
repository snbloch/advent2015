import io
import itertools

package_weights = []
group1_possibilities = []
group1_min_size = 0
group1_min_qe = 0

file = open('input.txt', 'r')
for line in file:
    package_weights.append(int(line))

package_sum = 0
for i in package_weights:
    package_sum += i

target_weight = package_sum / 3

counter = 0
while counter < len(package_weights):
    for i in itertools.combinations(package_weights, counter):
        current_weight = 0
        for j in i:
            current_weight += j
        if current_weight == target_weight:
            group1_possibilities.append(i)
    counter += 1

for combo in group1_possibilities:
    if group1_min_size == 0:
        group1_min_size = len(list(combo))
        group1_qe = 1
        for i in list(combo):
            group1_qe *= i
        group1_min_qe = group1_qe
    elif len(list(combo)) < group1_min_size:
        group1_qe = 1
        for i in list(combo):
            group1_qe *= i
        group1_min_qe = group1_qe
    elif len(list(combo)) == group1_min_size:
        group1_qe = 1
        for i in list(combo):
            group1_qe *= i
        if group1_qe < group1_min_qe:
            group1_min_qe = group1_qe

print group1_min_qe
