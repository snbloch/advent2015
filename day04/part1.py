from hashlib import md5
from collections import Counter

hash_input = 'yzbqklnj'
counter = 1

found = False
while found == False:
    test_input = hash_input + str(counter)
    md5sum = str(md5(test_input).hexdigest())
    if Counter(md5sum[0:5])['0'] == 5:
        found = True
        print counter
    counter += 1
