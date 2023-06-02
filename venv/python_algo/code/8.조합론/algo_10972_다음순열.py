# https://star7sss.tistory.com/446
import sys
from itertools import permutations

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    perm = list(map(int, input().split()))

    # 순열 계산
    permutation = list(permutations(range(1, n + 1), n))

    # 다음 순열 찾기
    cnt = 0
    for idx, i in enumerate(permutation):
        if i == tuple(perm):
            cnt = idx + 1

    # 출력
    if cnt == len(permutation):
        print(-1)
    else:
        print(" ".join(map(str, permutation[cnt])))