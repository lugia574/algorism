# 전에 풀었더 과제 문제랑 비슷한거 같은데
# 정렬만 다르게 해주면 되네
# 우선순위 큐로도 풀수 있다네
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    days = [False] * 10_001
    arr.sort(key= lambda x: (x[0], x[1]),reverse=True)
    res = 0
    for pay, day in arr:
        if days[day]:
            while day > 0 and days[day]:
                day -= 1
        if day == 0: continue
        else:
            days[day] = True
            res += pay

    print(res)

