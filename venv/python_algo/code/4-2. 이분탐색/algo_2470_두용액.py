# 대체 뭘 기준으로 잡으라는거지?
# 0 에 가까운 마수랑 플수를 내라는건데
# 그냥 리스트 안에서 양 끝단을 잡고 비교해서 조으면 될듯?
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().rsplit()))
    arr.sort()

    lt = 0
    rt = n-1

    meltingNum = 2e+9+1
    ans = []

    # lt <= rt 이럼 안됨 중복되는 값을 계산해버려
    while lt < rt:
        melting = arr[lt] + arr[rt]

        if abs(melting) < meltingNum:
            meltingNum = abs(melting)
            ans = [arr[lt], arr[rt]]
            if meltingNum == 0:
                break
        if melting < 0:
            lt += 1
        else:
            rt -= 1

    print(*ans)

