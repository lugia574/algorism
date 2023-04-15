# (a종류수 + 1) * (b종류수 + 1) * (c종류수 + 1)... - 1
# https://hongcoding.tistory.com/60
import sys
if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        n = int(input())
        clothes = {}
        for _ in range(n):
            wear = list(input().split())
            if wear[1] in clothes:
                clothes[wear[1]].append(wear[0])
            else:
                clothes[wear[1]] = [wear[0]]

        res = 1
        for k in clothes:
            res *= (len(clothes[k]) + 1)
        print(res-1)