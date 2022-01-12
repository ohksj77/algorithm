import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = [True] * n
result = []
def dfs(s):
    if s == m:
        print(*result)
        return
    last = 0
    for i in range(n):
        if visited[i] and last != arr[i]:
            visited[i] = False
            result.append(arr[i])
            last = arr[i]
            dfs(s + 1)
            result.pop()
            visited[i] = True
dfs(0)
