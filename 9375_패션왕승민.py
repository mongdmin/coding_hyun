import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    dic = {}
    n = int(input())
    for i in range(n):
        name, kind = input().split()
        dic[kind] = dic.get(kind, 0)+1
    cnt = 1
    for k in dic.values():
        cnt*=(k+1)
    print(cnt-1)