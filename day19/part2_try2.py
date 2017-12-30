import io

starting_formula = 'e'
medicine_molecule = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
#medicine_molecule = 'HOHOHO'
steps = 0

replacements = []

file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    left = line.split(' => ')[0]
    right = line.split(' => ')[1]
    replacements.append((left, right))

rep = 0
while rep < len(replacements):
    source, dest = replacements[rep]
    i = medicine_molecule.find(dest)
    if i != -1:
        steps += 1
        medicine_molecule = medicine_molecule[:i] + source + medicine_molecule[i + len(dest):]
        rep = 0
    else:
        rep += 1

print steps
