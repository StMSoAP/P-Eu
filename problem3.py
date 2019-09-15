number = int ( input ("Okay, what do you want the biggest prime factor of? "))

factor = 0
while number != factor:
    done = False
    for factor in range(2, number):
        while number % factor == 0:
            number = number // factor
            done = True
        if done == True:
            break
    if done == False:
        break

print (number)
    
