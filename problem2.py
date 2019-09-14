the_list = [1, 2]

while the_list[-1] < 4000000:
    the_list.append(the_list[-1]+the_list[-2])
del the_list[-1]

even_set = set()
index = 1
while index < len(the_list):
    even_set.add(the_list[index])
    index = index + 3


print (the_list)
print (even_set)
print (sum(even_set))
