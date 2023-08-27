# 뭔소리야 말하는게 살짝 이상하네
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    userSet = set()
    res = 0
    for _ in range(n):
        user = input().strip()
        if user == "ENTER":
            res += len(userSet)
            userSet = set()
        else:
            userSet.add(user)

    res += len(userSet)
    print(res)