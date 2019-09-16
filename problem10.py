primes = 2
elem = 1
for prime_candidate in range (3, 2000020, 2):
    nope = False
    for elem in range (2, int(prime_candidate / 2)):
        if prime_candidate % elem == 0:
            nope = True
            break
    if nope == False:
        print (prime_candidate)
        if prime_candidate > 2000000:
            break
        primes = primes + prime_candidate
print (primes)
