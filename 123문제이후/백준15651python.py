import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
def dfs():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        arr.append(i)
        dfs()
        arr.pop()
dfs()
