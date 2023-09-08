# 뭔소린지 알겠는데 이거 비슷한 문제 나오면 내가 이걸 적용할수 있을랑가 모르겠네

import sys, heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    k, n = map(int, input().split())
    prime = list(map(int, input().split()))

    pq = []
    answer = 0
    for num in prime:
        heapq.heappush(pq, num)

    for _ in range(n):
        answer = heapq.heappop(pq)
        for i in range(k):
            newVal = prime[i] * answer
            heapq.heappush(pq, newVal)

            if answer % prime[i] == 0:
                break
    print(answer)