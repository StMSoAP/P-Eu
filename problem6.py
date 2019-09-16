upper = sum(range(0, 101))**2
print (upper)
the_list = []
the_list.extend(range(0, 101))
the_list = [elem ** 2 for elem in the_list]
lower = sum(the_list)
print (lower)
print (upper - lower)
