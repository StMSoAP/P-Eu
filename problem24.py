import time
from itertools import permutations
start = time.time()
perm = permutations([0,1,2,3,4,5,6,7,8,9])

perm = list(perm)
print (perm[999999])
end = time.time()
print ("We did it in {} seconds!  And by we I mean me.".format(end-start))
