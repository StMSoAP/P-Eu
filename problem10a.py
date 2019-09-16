primes = []
elem = 1
for prime_candidate in range (3, 1415, 2):
    nope = False
    for elem in range (2, int(prime_candidate / 2)):
        if prime_candidate % elem == 0:
            nope = True
            break
    if nope == False:
        print (prime_candidate)
        if prime_candidate > 1415:
            break
        primes.append(prime_candidate)
print (primes)

potential_primes = list(range(1415, 2000000, 2))
for cnt in primes:
    #print ("\n")
    #print (cnt)
    for elem in potential_primes:
        if potential_primes[elem] % cnt == 0:
            
            print (len(potential_primes))

            del potential_primes[elem]
print (potential_primes)
print (sum(potential_primes)+sum(primes))
            
        
