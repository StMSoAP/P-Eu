biggest = 998001
palindrome = 0
big_factor = 999
little_factor = 999
'''
while biggest > 0:
    while biggest != int(str(biggest)[::-1]): #is it a palindrome?
        biggest = biggest - 1
        print (biggest)
    big_factor = 999
    while biggest % big_factor != 0:
        big_factor = big_factor - 1
        if big_factor == 101:
            break
    little_factor = big_factor - 1
    while biggest % little_factor != 0:
        little_factor = little_factor - 1
        if little_factor == 100:
            break
    if little_factor == 100:
        break
    biggest = biggest - 1
'''    
for big_factor in range (1000, 700, -1):
    for little_factor in range (1000, 700, -1):
        if big_factor * little_factor > palindrome:
            biggest = big_factor * little_factor
        if biggest == int(str(biggest)[::-1]): #is it a palindrome?
            palindrome = biggest
            print (palindrome)
            print (big_factor)
            print (little_factor)

print (biggest)

        
    

