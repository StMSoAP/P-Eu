for a in range(1, 333):
    for b in range(2, 500):
        for c in range(3, 997):
            if a + b + c == 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    print (a)
                    print (b)
                    print (c)
                    print (a*b*c)
