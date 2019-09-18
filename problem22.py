import time
start = time.time()
names = open("p022_names.txt").read()
names = names[1:-1]
names = names.split("\",\"")
names.sort()

alpha_values = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
total_count = 0

for name in range (0, len(names)):
    namelings = list(names[name])
    count = 0
    for letter in range (0, len(namelings)):
        count += alpha_values[namelings[letter]]
    total_count += count * (name + 1)
print (total_count)
stop = time.time()
print ("That took {} seconds!".format(stop-start))
