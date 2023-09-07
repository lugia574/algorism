import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nameSet = set()
    for _ in range(n):
        a, b = input().strip().split(" ")
        if a == 'ChongChong' or b == 'ChongChong' or a in nameSet or b in nameSet:
            nameSet.add(a)
            nameSet.add(b)

    print(len(nameSet))