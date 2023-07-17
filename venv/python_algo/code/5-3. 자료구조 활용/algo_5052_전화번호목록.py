import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        telNums = [input().strip() for _ in range(n)]
        telNums.sort()

        ok = True
        for i in range(n-1):
            long = len(telNums[i])
            if telNums[i] == telNums[i+1][:long]:
                ok = False
                break

        print("YES" if ok else "NO")