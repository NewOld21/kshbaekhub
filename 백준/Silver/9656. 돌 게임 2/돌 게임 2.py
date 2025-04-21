import sys

stone = int(sys.stdin.readline())
name = ['SK', 'CY']

if(stone%4 == 1 or stone%4 == 3) :
    print(name[1])
else :
    print(name[0])