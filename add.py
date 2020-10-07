import sys
import os
import datetime
from sortFile import doSort

os.chdir(os.path.expanduser('~')+ '/Projects/Dailies/')

arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i] + ' '
arg = arg.rstrip()


flag = False
while not flag:
    category = input('Enter Category: ')
    if category.lower() == 'reward' or category.lower() == 'rewards':
        pointValue = int(input('Enter point value: '))
        f = open('Rewards/shop.txt', 'r')
        currentRewards = f.readlines()
        f.close()
        f = open('Rewards/shop.txt', 'w')
        for i in currentRewards:
            f.write(i)
        f.write(str(pointValue) + '\t\t' + arg.strip() + '\n')
        quit()
    if not os.path.isfile('Categories/' + category.lower() + '.txt'):
        print('Category does not exist. Try again.')
    else:
        flag = True
        
flag = False
while not flag:
    timeCode = int(input('Enter time code: '))
    if timeCode >= 0 and timeCode <= 5:
        flag = True
    else:
        print('Please enter a number between 0 and 5 for the time code.')

pointValue = int(input('Enter point value: '))
    
f = open('Categories/' + category.lower() + '.txt', 'r')
currentContents = f.readlines()
f.close()
f = open('Categories/' + category.lower() + '.txt', 'w')
for i in currentContents:
    f.write(i)
f.write(str(timeCode) + '\t' + arg.ljust(25) + '\t' + str(pointValue) + '\n')
f.close()
doSort('Categories/' + category + '.txt')

today = datetime.date.today()
day = ''
if today.weekday() == 6:
    day = 'sunday'
if today.weekday() == 0:
    day = 'monday'
if today.weekday() == 1:
    day = 'tuesday'
if today.weekday() == 2:
    day = 'wednesday'
if today.weekday() == 3:
    day = 'thursday'
if today.weekday() == 4:
    day = 'friday'
if today.weekday() == 5:
    day = 'saturday'

g = open('Days/' + day + '.txt', 'r')
todaysCategories = g.readlines()
g.close()
toSearch = []
for i in todaysCategories:
    toSearch.append(i.strip())
if category in toSearch:
    d = today.strftime('%b-%d-%Y')
    t = open('History/' + d, 'r')
    todayCurrent = t.readlines()
    t.close()
    t = open('History/' + d, 'w')
    for i in todayCurrent:
        t.write(i)
    t.write(str(timeCode) + '\t' + arg.ljust(25) + '\t' + str(pointValue) + '\t' + '0' + '\n')
    t.close()
    doSort('History/' + d)

