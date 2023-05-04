import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    global res

    for n in graph[node]:
        if check[n] == 0:
            check[n] = 1 if check[node] == 2 else 2
            dfs(n)
        else:
            if check[n] == check[node]:
                res = False
                return

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        v, e = map(int, input().split())
        check = [0] * (v+1)
        graph = [[] for _ in range(v+1)]
        for _ in range(e):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)

        res = True
        for i in range(1, v+1):
            if check[i] == 0:
                check[i] = 1
                dfs(i)
                if not res:
                    break

        print("YES" if res else "NO")

        # 1
        # 1 1
        # 1 1
        # NO

        # 1
        # 3 1
        # 1 2
        # YES

        # 데이터 초기화 test
        # 2
        # 3 3
        # 1 2
        # 2 3
        # 3 1
        # 3 3
        # 1 2
        # 2 3
        # 3 1
        # NO
        # NO (YES 가 나오면 초기화 X)