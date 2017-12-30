import io

starting_formula = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'

replacements = []
new_formulas = set()

file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    left = line.split(' => ')[0]
    right = line.split(' => ')[1]
    replacements.append((left,right))

for i in replacements:
    num_occurrences = starting_formula.count(i[0])
    counter = 0
    last_found = 0
    while counter < num_occurrences:
        index = starting_formula.find(i[0], last_found)
        left_string = starting_formula[:index]
        right_string = starting_formula[index:]
        last_found = index + 1
        right_string = right_string.replace(i[0], i[1], 1)
        new_formulas.add(left_string + right_string)
        counter += 1

print len(new_formulas)
