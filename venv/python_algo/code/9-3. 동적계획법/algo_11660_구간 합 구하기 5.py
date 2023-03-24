# 보니까 여러번의 구간 합을 구해야하거든?
# 그러다보면 중복되는 값들이 무조건 있을꺼야
# 그걸 dp 에 저장해서
# 코드를 진행할때마다 만약에 dp 값이 있으면 그 값을 그대로 쓰고
# 없으면 그 값을 넣어주는거지
# 근데 그럴려면 dp 를 2차원으로 할께 아니라 3차원 dp로 해야하는거 아닌가? 흠흠흠

# 아 시초 떳어
# (n^ - 1) + (m + 1) n
# 될만한데

# sys.stdin.readline 이거 안해줘서 시초 떳었네 ㅋㅋㅋ 개꿀

# 자 풀이법 설명 드간다
# 위에는 뭔가 분할방식으로 푸는 느낌 생각했는데
# 어차피  start 지점에서 end 점까지 싹다 더하는거임
# 그러니까 첫번째 지점을 제외한 각 지점을 += current - 1 을 싹 해주고
# end - (start - 1 지점) 해주면 딱 st - end 까지의 합을 구할수 있음


import sys



if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for i in range(n + 1)] for i in range(n + 1)]

    for i in range(n):
        for j in range(1, n):
            arr[i][j] += arr[i][j - 1]
        arr[i].insert(0, 0)

    for _ in range(m):
        res = 0
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2 + 1):
            res += arr[i - 1][y2] - arr[i - 1][y1 - 1]

        print(res)









