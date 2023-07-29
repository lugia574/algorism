# n 이 1000 m이 1000
# 알고리즘 분류를 보면 안됐는데 이분탐색이랑 누적합을 봐버렸네
# 문제를 읽으니까 뭔소린지 좀 알겠네
# 파이썬 답들은 존나 라이브러리를 써서 직관적이지가 않음
# https://loosie.tistory.com/560 이 자바코드를 파이썬 코드로 변환함
# 는 https://velog.io/@nyanyanyong/알고리즘python백준-2143두-배열의-합
# 여기 들가보면 그냥 딕셔너리로 풀어버림
# 원리는 A i~j 까지의 합을 key 값으로 하고 갯수를 카운팅해서 딕셔너리에 박아
# 그리고 B i~j 까지의 합을 T 값에 빼서 나온 A 값을 answer 에 더하면 됨
# 이게 뭔소리냐면
# T 가 5이고 B i~j 까지 합이 2 라면 A 값은 뭐야 할까 3 이겠지
# 그러니까 dictA[T - Bsumr값(i:j)] 이 되는거임
import sys
from _collections import defaultdict

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    a = int(sys.stdin.readline())
    listA = list(map(int, sys.stdin.readline().split()))
    b = int(sys.stdin.readline())
    listB = list(map(int, sys.stdin.readline().split()))

    dictA = defaultdict(int)


    ans = 0

    for i in range(a):
        for j in range(i, a, 1):
            dictA[sum(listA[i:j+1])] += 1

    for i in range(b):
        for j in range(i, b, 1):
            ans += dictA[T - sum(listB[i:j+1])]

    print(ans)
    # 1 4 5 7
    #   3 4 6
    #     1 3
    #       2

    # 1 4 6
    #   3 5
    #     1
