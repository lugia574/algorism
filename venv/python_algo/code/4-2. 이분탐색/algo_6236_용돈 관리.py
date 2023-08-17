# 먼소린지 이해가 바로 안되는데 ㅋ
# 그니까 총 N일동안 돈을 사용하는데
# 딱 M 번만 돈을 꺼내 쓴다는 소리자너
# k 원을 인출해서 딱코면 그대로 쓰고
# 부족하면 남은 금액을 다시 넣고 k 원을 다시 뽑아
# 금액이 남으면 금액을 다시 넣고 k 원을 뽑을 수도 있어 (이건 m 번 맞추기 위해서 억지로 하는 용도?)
# 최고 k 금액을 구하라
# 100, 400, 300, 100, 500, 101, 400 이라고 했을떄
# 1(100 400), 2(300, 100), 3(500), 4(101), 5(400) 이렇게 되는거 같은데?

# 딱 봐도 k 를 기준으로 이분탐색 해야한다는 느낌이 드는데
# 이건 sort 할수도 없고
# 어떻게 해야 풀리나
# 어허 대충 틀은 맞았는데 cnt 하는 과정을 개같이 못함
# 그냥 부족하다 싶으면 인출해버리고 정산하는데 난 왜 이렇게 못짯지?
# 아직 내 이분탐색 능력이 허접하기 그지 없고
# 구현 능력도 존나 후달리는걸 증명하는거지 뭐
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    start = min(arr)
    end = sum(arr)
    maxCost = max(arr)

    while start <= end:
        mid = start + (end - start) // 2
        cnt = 1
        charge = mid
        for cost in arr:
            if charge < cost:
                charge = mid
                cnt += 1
            charge -= cost

        if cnt > m or mid < maxCost:
            start = mid + 1
        else:
            end = mid - 1

    print(start)