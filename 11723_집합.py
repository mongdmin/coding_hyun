import sys
input = sys.stdin.readline

S=set()

M = int(input())

def solve(op, x=None):
    if op == "add": S.add(x)
    elif op == "remove": S.discard(x)
    elif op == "check":
        if x in S: print(1)
        else: print(0)
    elif op == "toggle":
        if x in S: S.remove(x)
        else: S.add(x)
    elif op == "all":
        S.clear()
        S.update(range(1,21))
    else: S.clear()

for i in range(M):
    op = input().split()
    if len(op) == 2: solve(op[0],int(op[1]))
    else: solve(op[0])