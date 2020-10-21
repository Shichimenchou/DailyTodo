import os
import re
import datetime

today = datetime.date.today()
d = today.strftime('%b-%d-%Y')

os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')

if not os.path.isfile('History/' + d):
    dailies = open('History/' + d, 'w+')
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

    weekday = open('Days/' + day + '.txt')
    categories = weekday.readlines()
    weekday.close()
    
    todaysTasks = []
    for i in categories:
        c = open('Categories/' + i.strip() + '.txt')
        t = c.readlines()
        for j in t:
            todaysTasks.append(re.split(r'\t+', j))

    flag = False
    while not flag:
        flag = False
        for i in range(0, len(todaysTasks)):
            for j in range(i, len(todaysTasks)):
                if int(todaysTasks[j][0]) < int(todaysTasks[i][0]):
                    temp = todaysTasks[i]
                    todaysTasks[i] = todaysTasks[j]
                    todaysTasks[j] = temp
                    flag = True
    
    for i in todaysTasks:
            dailies.write(i[0] + '\t' + i[1].ljust(25) + '\t' + i[2].rstrip() + '\t' + '0' + '\n')

    dailies.close()

    #now = datetime.datetime.now()
    #if int(now.hour) < 7:
    #    import update
