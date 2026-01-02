import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    info.append(list(map(int,input().split())))

rank = []

for x,y in info:
    cnt = 1
    for nx,ny in info:
        if x<nx and y<ny: cnt += 1
    rank.append(cnt)

print(*rank)