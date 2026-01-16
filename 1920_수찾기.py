import sys
from bisect import bisect_left
input = sys.stdin.readline

N=int(input())
num = list(map(int,input().split()))
num.sort()

M=int(input())
check = list(map(int,input().split()))

for x in check:
    idx = bisect_left(num,x)
    if idx < len(num) and num[idx]==x: print(1)
    else: print(0)