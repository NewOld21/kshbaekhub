import sys
import math
a,b = map(int, sys.stdin.readline().split())
n = math.gcd(a,b)
print('1'*n)
