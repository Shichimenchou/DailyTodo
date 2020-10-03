import sys
import os
import datetime

today = datetime.date.today()
d = today.strftime('%b-%d-%Y')

os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')
f = open('History/' + d, 'r')
old = f.readlines()

count = 0
line = -1
arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i].lower() + ' '
arg = arg.rstrip()
for t in range(0, len(old)):
    if old[t].lower().find(arg) >= 0:
        count += 1
        line = t

if count == 0:
    print('This task does not exist. Try again')
    f.close()
if count == 1:
    new = []
    for i in range(0, len(old)):
        if i != line:
            new.append(old[i])
    f.close()
    g = open('History/' + d, 'w')
    for i in new:
        g.write(i)
    g.close()
    
if count > 1:
    print('There are multiple tasks containing your phrase. Try again.')
    f.close()

