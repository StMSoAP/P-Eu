power = str(2 ** 1000)
power_list = list(power)
print(power_list)
for elem in range(0, len(power_list)):
    power_list[elem] = int(power_list[elem])
print (sum(power_list))
