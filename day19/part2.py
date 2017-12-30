import io

starting_formula = 'e'
medicine_molecule = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
steps = 0

replacements = []
new_formulas = set()
new_formulas.add((starting_formula, steps))
found = False

file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    left = line.split(' => ')[0]
    right = line.split(' => ')[1]
    replacements.append((left, right))

while found == False:
    temp_formulas = []
    for formula in new_formulas:
        for i in replacements:
            steps = formula[1]
            num_occurrences = formula[0].count(i[0])
            counter = 0
            last_found = 0
            while counter < num_occurrences:
                index = formula[0].find(i[0], last_found)
                left_string = formula[0][:index]
                right_string = formula[0][index:]
                last_found = index + 1
                right_string = right_string.replace(i[0], i[1], 1)
                if left_string + right_string != medicine_molecule:
                    temp_formulas.append((left_string + right_string, steps + 1))
                else:
                    found = True
                    print steps + 1
                new_formulas = set(temp_formulas)
                counter += 1
