import math
excited_about_100 = list(str(math.factorial(100)))
woo = sum([int(item) for item in excited_about_100])
print (woo)
