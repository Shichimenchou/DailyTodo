import sys
import os


os.chdir(os.path.expanduser('~')+ '/Projects/Dailies/')

arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i] + ' '
arg = arg.rstrip()


flag = False
while not flag:
    category = input('Enter Category: ')
    if not os.path.isfile('Categories/' + category + '.txt'):
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

pointValue =int(input('Enter point value: '))
    
f = open('Categories/' + category + '.txt', 'r')
currentContents = f.readlines()
f.close()
f = open('Categories/' + category + '.txt', 'w')
for i in currentContents:
    f.write(i)
f.write(str(timeCode) + '\t' + arg.ljust(25) + '\t' + str(pointValue) + '\n')
f.close()
