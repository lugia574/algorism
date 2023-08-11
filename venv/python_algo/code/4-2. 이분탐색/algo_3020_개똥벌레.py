# 먼소리야 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으루 구분하라는게
# 그니까 최솟값인 값의 갯수가 몇개냐는거야? 2 3 이면 최솟값은 2이고 그 갯수는 3개라는거야?
# 그러네 맞네
# 근데 최솟값은 구했는데 그 갯수 구하기가 빡센데? 지금 딱 생각나는건 2중 포문 갈기는건데
# 그러면 결국 첨부터 2중포문 갈겼음 최솟값도 구하고 그 갯수 구하기 쌉가능이자너 근데 왜 안해겠너 시초 뜨니까 안하지 ㅋㅋ
# 딕셔너리도 안통하고 흠흠

# https://hongcoding.tistory.com/6
# 자 결국 답안을 검색 해버렸어요~~
# 이 풀이는 누적합을 이용한 풀이네요
# 종유석과 석순의 index 를 높이로 해서 count 해줍시다~
# 그리고 높은순에서부터 차례대로 내려오면서 누접합을 해봅시다
# h-1 부터 시작해서 i += i+1 를 해줍시다
# 설명하자면 7과 8 길의 탑이 있다면 당연히 7 높이로 가면 7 8 모두 걸립니다
# 즉 현재 자신의 높이보다 큰 애들은 다 걸리는겁니다~
# 그러니까 h-1 부터 시작해서 i+1 이렇게 한칸씩 누접합 해주는겁니다~

# 자 그리고 이제부터 높이 1부터 하나씩 올라가면서
# i 높이 일때 sum(석순 + 종유석)을 비교해서 갱신 해주면 됩니다~
# 이러면 시간복잡도 n+2h 으로 쉽게 1_200_000 로 쌉가능이네요~
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, h = map(int, input().split())
    down = [0] * (h + 1)  # 석순
    up = [0] * (h + 1)  # 종유석

    min_count = n  # 파괴해야 하는 장애물의 최소값
    range_count = 0  # 최소값이 나타나는 구간의 수

    #count
    for i in range(n):
        if i % 2 == 0:
            down[int(input())] += 1
        else:
            up[int(input())] += 1
    # 누적합
    for i in range(h - 1, 0, -1):
        down[i] += down[i + 1]
        up[i] += up[i + 1]

    for i in range(1, h + 1):

        if min_count > (down[i] + up[h - i + 1]):
            min_count = (down[i] + up[h - i + 1])
            range_count = 1
        elif min_count == (down[i] + up[h - i + 1]):
            range_count += 1

    print(min_count, range_count)


   #   1 2 3 4 5 6
   # 7   5   3   1
   # 6   5   3
   # 5   5   3 5
   # 4   5     5
   # 3   5 3   5
   # 2     3   5
   # 1 1   3   5
