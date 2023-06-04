# 참고로 등수임 5면 5등인거임 잘한게 아녀 ㅋㅋㅋ
# 이게 어떻게 되는거면
# idx 0 을 기준으로 sort 하면
# 기본적으로 뒷자리 애들은 죽었다 깨어나도 0 번째 시험 등수로 앞에 놈들을 이길 수 없음
# 그렇게 정렬한 후 1번째 시험 등수만 따져 보는거야
# [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
# 를 예시로 설명하면
# [1, 4] 에서 0 번 idx 는 무조건 1등이야 그 누구도 얘를 못이겨
# 1번 idx 로 비벼야지
# [2,5] 안되고, [3, 6] 도 안돼 [4, 2] 얘는 이기자너 그럼 얘는 통과 인거야
# 통과 되면서 갱신 시켜줘야지 앞서 말했음 무조건 0 번 idx 로 뒤에 얘들이 이길 수 없어
# 이제 [4, 2]  얘 보다 나은 1 번 idx 등수를 가진 얘을 찾아야하는거야
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        p = [list(map(int, input().rsplit())) for _ in range(n)]
        p = sorted(p, key = lambda x: (x[0], x[1]))
        cnt = 1
        # print(p)
        cutline = p[0][1]
        for i in range(1, n):
            if cutline > p[i][1]:
                cutline = p[i][1]
                cnt += 1
        print(cnt)