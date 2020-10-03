import sys
import os
import re
from datetime import date

today = date.today()
d = today.strftime('%b-%d-%Y')

os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')
f = open('History/' + d, 'r')
todo = f.readlines()

count = 0
line = -1
arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i].lower() + ' '
arg = arg.rstrip()

if arg == '':
    for i in todo:
        print(i.rstrip())
    f.close()
else:
    for t in range(0, len(todo)):
        if todo[t].lower().find(arg) >= 0:
            count += 1
            line = t

    if count == 0:
        print('This task does not exist. Try again')
        f.close()
    if count == 1:
        temp = re.split(r'\t+', todo[line])
        if int(temp[3]) == 0:
            p = open('points.txt', 'r')
            val = int(p.readline()) + int(temp[2])
            p.close()
            q = open('points.txt', 'w')
            q.write(str(val))
            q.close()
            temp[3] = 1
            todo[line] = str(temp[0]) + '\t' + str(temp[1]).ljust(25) + '\t' + str(temp[2]) + '\t' + str(temp[3]) + '\n'
            f.close()
            g = open('History/' + d, 'w')
            for i in todo:
                g.write(i)
            g.close()
        else:
            print("Already completed today.")
            f.close()
    if count > 1:
        print('There are multiple tasks containing your phrase. Try again')
        f.close()
