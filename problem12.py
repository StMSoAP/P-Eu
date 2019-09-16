#generate triangle number
#find factors
#check number of factors
import time
import math
start = time.time()
triangle = int (0)

for guess in range(1, 100000):
    
    factor_count = 0
    triangle = triangle + guess 
    
    for factor in range(1, int(math.sqrt(triangle))):
        if triangle % factor == 0:
            factor_count = factor_count + 2
    if factor_count > 499:
        break
        
    print(factor_count)
    
stop = time.time()

print(triangle)
print("Time: {} seconds".format(stop - start))
