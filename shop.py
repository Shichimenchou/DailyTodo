import sys
import os
import re

os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')
f = open('Rewards/shop.txt', 'r')
shop = f.readlines()

p = open('points.txt', 'r')
points = int(p.readline())
p.close()

count = 0
line = -1
arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i].lower() + ' '
arg = arg.rstrip()

if arg == '':
    for i in shop:
        print(i.rstrip())
    print('Points remaining: ' + str(points))
    f.close()
else:
    for s in range(0, len(shop)):
        if shop[s].lower().find(arg) >= 0:
            count += 1
            line = s

    if count == 0:
        print('This reward does not exist.\nPoints remaining: ' + str(points))
    if count == 1:
        item = re.split(r'\t+', shop[line])
        if int(item[0]) <= points:
            points -= int(item[0])
            q = open('points.txt', 'w')
            q.write(str(points))
            q.close()
            print('You have purchased \"' + item[1].rstrip() + '.\"\nPoints remaining: ' + str(points))
        else:
            print('You don\'t have enough points for this reward.\nPoints remaining: ' + str(points))
    if count > 1:
        print('There are multiple rewards containing your phrase.\nPoints remaining: ' + str(points))
