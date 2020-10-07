import os
import datetime

def doSort(fileName):
    today = datetime.date.today()
    d = today.strftime('%b-%d-%Y')

    os.chdir(os.path.expanduser('~') + '/Projects/Dailies/')

    f = open(fileName, 'r')
    unsorted = f.readlines()
    f.close()
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(0, len(unsorted)):
            for j in range(i, len(unsorted)):
                if int(unsorted[j][0]) < int(unsorted[i][0]):
                    temp = unsorted[i]
                    unsorted[i] = unsorted[j]
                    unsorted[j] = temp
                    isSorted = False

    f = open(fileName, 'w')
    for i in unsorted:
        f.write(i)
    f.close()

