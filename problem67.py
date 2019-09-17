raw_pyramid = []

with open('p067_triangle.txt') as inputfile:
    for line in inputfile:
        raw_pyramid.append(line.strip().split(' '))

def collapse (top, left, right):
    if left > right:
        return top + left
    else:
        return top + right

pyramid = [[int(i) for i in row] for row in raw_pyramid]

for row in range (98, -1, -1):
    for column in range (0, row+1):
        pyramid[row][column] = collapse (pyramid[row][column],
                                         pyramid[row+1][column],
                                         pyramid[row+1][column+1])

print (pyramid[0][0]) 

