import sys
input = sys.stdin.readline

def gcd(A,N):
    r1, r2 = N, A
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1//r2
        r1, r2 = r2, r1-q*r2
        t1, t2 = t2, t1-q*t2

    if r1 != 1: return -1
    return t1 % N

N,A = map(int,input().split())

print(N-A, gcd(A,N))

# 블로그 코드 -> pow내장 함수 이용

# n, m = map(int, input().split())
# print(n - m)
# try:
#     print(pow(m, -1, n))
# except:
#     print(-1)