presents_target = 36000000

def get_all_factors(n):
    factors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            if n / i != i:
                factors.append(n / i)
        i += 1
    return factors

found = False

counter = 1
while found == False:
    sum_of_factors = 0
    fac = get_all_factors(counter)
    for f in fac:
        sum_of_factors += f
    if sum_of_factors * 10 >= presents_target:
        found = True
        print counter
    counter += 1
