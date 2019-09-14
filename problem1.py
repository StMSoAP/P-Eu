the_set = set()

a_number = 0

while a_number<1000:
    the_set.add(a_number)
    a_number = a_number + 5

a_number = 0

while a_number<1000:
    the_set.add(a_number)
    a_number = a_number + 3

print ( sum ( the_set))
