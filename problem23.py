import time

def abundance(uh):
    factor_sum = 0
    for factor in range(1, int(uh/2+1)):
        if uh%factor == 0:
            factor_sum += factor
    if factor_sum > uh:
        print (uh)
        return True
    else:
        return False

start = time.time()

abundant_numbers = list()

for number in range (1, 28123):
    if abundance(number):
        abundant_numbers.append(number)

print(abundant_numbers)

fine = False

for number in range (len(abundant_numbers), 0, -1):
    for other_number in range (number, 0, -1):
        if abundant_number[number] == abundant_numbers[number] + abundant_number[other_number]:
            fine = True
            break
    if not fine:
        target = abundant_number[number]
        break

print (target)
end = time.time()
print ("We did it in {} seconds!  And by we I mean me.".format(end-start))











stop = time.time()
print ('Time: {} seconds.'.format(stop-start))
