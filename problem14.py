#find and count sequence
#compare and update largest test number
import time
start = time.time()

best = 0

def collatz(candidate):
    count = 1
    while candidate > 1:
        if candidate % 2 != 0:
            candidate = 3 * candidate + 1
            count += 1
        else:
            candidate = candidate / 2
            count += 1
    return count

for elem in range (1, 1000000):
    maybe = collatz(elem)
    if maybe > best:
        best = maybe
        bestest = elem


stop = time.time()
print(bestest)
print(best)
print("Time: {} seconds.".format(stop - start))
