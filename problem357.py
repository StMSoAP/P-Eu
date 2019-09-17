winners = list()
factors = list()
primaybe = 0
for candidate in range (1, 10001):
    for factor in range (1, int(candidate/2 +1)):
        if candidate % factor == 0:
            factors.append(factor)

    check = False
    for number in factors:
        primaybe = candidate / number + number
        for elem in range (2, int(primaybe/2 +1)):
            if primaybe % elem == 0:
                check = True
                break
        if check == True:
            break
    if check == False:
        print (candidate)
            
    factors = list()

