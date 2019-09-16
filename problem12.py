#generate triangle number
#find factors
#check number of factors

for guess in range(1, 10000):
    factor_list = []
    
    triangle = sum(range(1, guess+1)) 
    
    for factor in range(1, triangle+1):
        if triangle % factor == 0:
            factor_list.append(factor)
    if len(factor_list) > 499:
        break
        
    print(len(factor_list), end="\n")
print(factor_list)
print(triangle)
        
