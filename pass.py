import sys
import os
from datetime import date

today = date.today()
d = today.strftime('%b-%d-%Y')

os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')
f = open('History/' + d, 'r')
todo = f.readlines()
t = []
for i in todo:
    t.append(i.split('\t'))


count = 0
tring = ''
for i in t:
    if int(i[3]) == 0:
        tring += i[1].strip()
        count += 1
        if count == 3:
            break
        tring += ', '
    
print(tring)
