import time

def get_sum(uh):
    factor_sum = 0
    for factor in range(1, int(uh/2+1)):
        if uh%factor == 0:
            factor_sum += factor
    return factor_sum

start = time.time()
sum_dict = {0:0}
final_sum = 0

for i in range(1, 10001):
    sum_dict[i] = 0

for candidate in range (1, 10001):
    
    if sum_dict[candidate] == 0:
        check = get_sum(candidate)
        double_check = get_sum(check)

        if candidate == double_check and candidate != check:
            sum_dict[candidate] = 1
            sum_dict[check] = 1
            print(candidate)
            print(check)


for money in range (1, 10001):
    if sum_dict[money] == 1:
        final_sum += money


print (final_sum)
stop = time.time()
print ('Time: {} seconds.'.format(stop-start))
