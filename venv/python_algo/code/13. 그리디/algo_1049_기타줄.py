import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rsplit())
    g = [list(map(int, input().rsplit())) for _ in range(m)]
    minCost, single, package = int(1e9), int(1e9), int(1e9)

    for i in range(m):
        if single > g[i][1]:
            single = g[i][1]
        if package > g[i][0]:
            package = g[i][0]

        singleCost = single * n
        packageCost = package if n <= 6 else package * ((n // 6) + 1)
        singleXpackageCost = (package * (n // 6)) + (single * (n % 6))

        minCost = min(minCost, packageCost, singleCost, singleXpackageCost)

    print(minCost)