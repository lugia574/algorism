# 네트워크 선 자르기(Bottom-Up)
# 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다.
# 예를 들어 4m의 네트워크 선이 주어진다면
# 1) 1m+1m+1m+1m
# 2) 2m+1m+1m
# 3) 1m+2m+1m
# 4) 1m+1m+2m
# 5) 2m+2m
# 의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가
# 다르면 다른 경우로 생각한다.
# 그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?
# ▣ 입력설명
# 첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.
# ▣ 입력예제 1
# 7
# ▣ 출력예제 1
# 21

def DFS(l):
    global cnt
    if l == 0:
        cnt += 1
    else:
        for i in [1, 2]:
            if l-i >-1:
                DFS(l-i)

# 이렇게 하면 이제 n 값이 커지기 시작하면 존나 재귀를 돌아버려서 타임 아웃이 되어버림
# 즉 점화식으로 풀어야해
# 해당 문제는 f(n) = f(n-2) + f(n-1) 의 식을 가짐
# 그러니까 7 의 값은 f(7) = f(5) + f(6) 의 값을 가진다는 거지
# 이걸 쭉 내려가면 f(1), f(2) 값만 알면 쉽게 값을 구할 수 있다 이말이야

def f(n):
    dy[n] = dy[n-1] + dy[n-2]

if __name__ == "__main__":
    n = int(input())
    cnt = 0
    dy = [0] * (n+1)
    dy[1] = 1
    dy[2] = 2
    for i in range(3, n+1):
        f(i)
    # DFS(n)
    print(dy[n])

