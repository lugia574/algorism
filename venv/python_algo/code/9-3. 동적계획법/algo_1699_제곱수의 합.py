# 뭔가 어려울꺼 같은 느낌?
# 1 1^ = 1
# 2 1^ 1^ = 2
# 3 1^ 1^ 1^ = 3
# 4 2^ = 1
# 5 2^ 1^ = 2
# 6 2^ 1^ 1^ = 3
# 7 2^ 1^ 1^ 1^ = 4
# 8 2^ 2^ = 2
# 9 3^ = 1
# 10 3^ 1^ = 2
# 11 3^ 1^ 1^ = 3
# 12 2^ 2^ 2^ =3
# 13 3^ 2^ = 2
# 14 3^ 2^ 1^ = 3
# 15 3^ 2^ 1^ 1^ = 4
# 16 4^ = 1
# 17 4^ 1^ = 2
# 18 4^ 1^ 1^ = 3
# 19 4^ 1^ 1^ 1^ = 4
# 20 4^ 2^
# 21 4^ 2^ 1^
# 22 !
# ~
# 25 5^

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    dp = [i for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, i):
            if j * j > i:
                break
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    print(dp[n])

