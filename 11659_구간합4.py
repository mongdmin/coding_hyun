import sys
input = sys.stdin.readline

N,M = map(int,input().split())

num = list(map(int,input().split()))

dp = [0] * (N+1)

for k in range(1, N+1):
    dp[k] = dp[k-1] + num[k-1]

for _ in range(M):
    i,j = map(int,input().split())
    print(dp[j]-dp[i-1])