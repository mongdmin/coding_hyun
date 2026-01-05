import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())
    cnt = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(cnt)








# 시간 초과 코드
# for _ in range(k):
#     cnt = 0
#     i,j,x,y = map(int,input().split())
#     for a in range(i-1,x):
#         for b in range(j-1,y): cnt += arr[a][b]
#     print(cnt)