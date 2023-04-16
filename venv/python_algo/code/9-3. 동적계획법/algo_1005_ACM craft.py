# https://freedeveloper.tistory.com/390
# 이걸 보니까 그대로 쳐 베낀거 같은데
# 그래서 그런지 위상정렬 문제가 나오니까 그냥 쳐 틀렸음 ㅋ
# 그걸 풀려면 우선 이거부터 넘어야할 꺼 같음
# 주석을 싹다 써주자고 시벌
import sys
from collections import deque

def craft():
    N, K = map(int, input().rsplit())  # 건물수, 건설순서규칙을 받았어
    time = [0] + list(map(int, input().rsplit()))  # 건물들의 건설시간
    seq = [[] for _ in range(N + 1)]  # 건설순서규칙
    inDegree = [0 for _ in range(N + 1)]  # 진입차수
    dp = [0 for _ in range(N + 1)]  # 해당 건물까지 걸리는 시간

    for _ in range(K):  # 건설순서규칙 저장
        a, b = map(int, input().split()) # a를 지어야 b 가 가능하다
        seq[a].append(b)
        inDegree[b] += 1 # b 값에 a 의 갯수를 세는거야 가령 3번 건물을 만들려면 1 2 가 필요하면 차수는 2 라는 거지

    q = deque() 

    for i in range(1, N + 1):  # 진입차수 0인거 찾아서 큐에 넣기 # 진입차수가 0 이라는건 바로 지을 수 잇다는거니까
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    # 자 이제 q 를 돌려
    while q:
        a = q.popleft()
        for x in seq[a]:
            inDegree[x] -= 1  # 진입차수 줄이고
            dp[x] = max(dp[a] + time[x], dp[x])  # DP를 이용해 건설비용 갱신
            if inDegree[x] == 0:
                q.append(x)

    return dp

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        dp = craft()
        ans = int(input())
        print(dp[ans])


        