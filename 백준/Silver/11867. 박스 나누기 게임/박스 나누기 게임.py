import sys

N, M = map(int, sys.stdin.readline().split())

if N * M % 2 == 0 :
    print('A')
else :
    print('B')