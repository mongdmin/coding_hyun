import sys
input = sys.stdin.readline

N = int(input())

if N==1: print(0)
else: print(2*3**(N-2))


# 0
# 2 2
# 6 2*3
# 18 2*3*3
# 54 2*3*3*3