# 나 이거 문제 자체가 이해가 안감 ㅋ
# n=3 0 -5 5 일때 왜 정답이 1임? 3 아님?
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0

    for i in range(N):
        tmp = arr[:i] + arr[i + 1:]
        left, right = 0, len(tmp) - 1
        while left < right:
            t = tmp[left] + tmp[right]
            if t == arr[i]:
                ans += 1
                break
            if t < arr[i]: left += 1 # t 를 증가시켜야 하므로 left 증가
            else: right -= 1 # t 를 감소시켜야 하므로 right 감소

    print(ans)
