import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    card = list(map(int, input().split()))
    m = int(input())
    numArr = list(map(int, input().split()))

    check = [0] * 20000001

    for i in card:
        if i < 0:
            check[(i * -1) + 10000000] += 1
        else:
            check[i] += 1

    for j in numArr:
        if j < 0:
            print(check[(j * -1) + 10000000], end=" ")
        else:
            print(check[j], end=" ")

    # 그냥 지금 딱 생각나는게 -1억 ~ 1억 총 2억개의 check 리스트를 만들고
    # card arr 를 싹 돌려서 해당 값을 check index 체크를 해
    # 그리고 그걸 그대로 출력하면 되지 않을까?
    # 해보니까 됐음 딱 아슬아슬하게
    # 근데 이건 원래 이분탐색 하라고 나온 문제임 그니까 이분 탐색으로 풀어보자
