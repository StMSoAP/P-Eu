#create month variables
#figure out number of days in century (01/01/1901 was a Tuesday)
#add leap-Februaries--(not 1900 but 2000)
#check 7-day cycle against firsts of months
#lobby for better calendar
import time
start = time.time()

jan=31
feb=28
feb_prime=29
mar=31
apr=30
may=31
jun=30
jul=31
aug=31
sep=30
octb=31
nov=30
dec=31

'''
days = 0
for year in range (1901, 2001):
    if year % 400 == 0:
        days += 366
    elif year % 4 == 0:
        days += 366
    else:
        days += 365

print (days)
'''

total_days = 36525
getyocheck = {}
day = 1
eat_it_gregorius = 1

while day < total_days:
    day += jan
    getyocheck[day]=True
    if eat_it_gregorius % 4 == 0:
        day += feb_prime
        eat_it_gregorius += 1
    else:
        day += feb
        eat_it_gregorius += 1
    getyocheck[day]=True
    day += mar
    getyocheck[day]=True
    day += apr
    getyocheck[day]=True
    day += may
    getyocheck[day]=True
    day += jun
    getyocheck[day]=True
    day += jul
    getyocheck[day]=True
    day += aug
    getyocheck[day]=True
    day += sep
    getyocheck[day]=True
    day += octb
    getyocheck[day]=True
    day += nov
    getyocheck[day]=True
    day += dec
    getyocheck[day]=True
    
days_greg_can_eat_it = 0
for another_day in range (0, total_days, 7):
    if another_day in getyocheck:
        days_greg_can_eat_it += 1

stop = time.time()

print (days_greg_can_eat_it - 1)
print ('Time: {} seconds.'.format(stop-start))

