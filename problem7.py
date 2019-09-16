primes = [2]
elem = 1
for prime_candidate in range (3, 100000000, 2):
    nope = False
    for elem in range (2, prime_candidate - 1):
        if prime_candidate % elem == 0:
            nope = True
            break
    if nope == False:
        primes.append(prime_candidate)
        print (str(len(primes)) + "-----" + str(prime_candidate))
    if len(primes) == 10001:
        break
