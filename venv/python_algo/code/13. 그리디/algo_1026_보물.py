# 문제에서는 분명히 B 를 정렬하지 말고 sum 의 최솟값을 찾으라고 했는데
# 그렇게 말한다한들 B 를 정렬 못하게 물리적으로 제한을 걸 수 있는것도 아니고 ㅋ
# 그냥 내림차순, 올림차순으로 싹다 정렬해서 작은것 * 큰것 으로 곱해 버리고 sum값에 더해 버리면 됨 ㅋ
# ====
# 뭐 그래도 정식으로 풀려면 어떻게 풀어야 하나 하고 찾아보니
# 존나 개 무식하게 각 배열의 최솟값, 최댓값을 index를 찾아서 pop 해서 처리를 하더라
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().rsplit()))
    b = list(map(int, input().rsplit()))

    a.sort()
    b.sort(reverse=True)
    sumNum = 0
    for i in range(n):
        sumNum += a[i] * b[i]
    print(sumNum)