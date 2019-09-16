#generate triangle number
#find factors
#check number of factors
import time
start = time.time()
triangle = int (0)

for guess in range(1, 100000):
    factor_list = []
    
    triangle = triangle + guess 
    
    #for factor in range(1, triangle+1):
        #if triangle % factor == 0:
            #factor_list.append(factor)
    factor_list.extend([yield factor for factor in range(1, triangle+1) if factor * triangle // factor == triangle])
    if len(factor_list) > 499:
        break
        
    print(len(factor_list), end="\n")
stop = time.time()
print(factor_list)
print(triangle)
print("Time: {} seconds".format(stop - start))
        
