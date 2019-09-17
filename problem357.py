'''winners = list()
factors = list()
primaybe = 0
balls = 0
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
#        print (candidate)
        print(candidate - balls)
        balls = candidate





        
    factors = list()


1
2
6
10
22
30
42
58
70
78
82
102
130
190
210
310
330
358
382
442
462
478
562
658
742
838
862
970
1038
1222
1282
1318
1618
1810
1870
1978
2038
2062
2098
2242
2398
2458
2578
2902
2938
2962
3018
3082
3322
3642
3862
4218
4258
4282
4678
5098
5590
5938
6042
6078
6378
6598
6658
6718
6778
6862
7078
7282
7582
7638
7642
7702
8038
8110
8218
8542
8562
8962
9202
9718'''

candidates = list(range(2, 10001, 2))
for i in candidates:
    if (i/2)%2 == 0:
        candidates.remove(i)
    
print (candidates)
