import time
start = time.time()

fib = [1,1]

while fib[-1] < 10 ** 999:
    fib.append(fib[-1]+fib[-2])
print (len(fib))
end = time.time()
print ("The end is nigh!  Er, now.  It took {} seconds.".format(end-start))
