# 이게 점수과 정확성, 효율성 2개 파트로 나뉘는데
# 단순히 카운팅해서 답 내는걸로는 효율성 파트에서 개박살이 나버림
# 효율성 파트까지 챙기려면 이분탐색을 이용해야한다
# 생각보다 별거 없는데 최소수(left), 최고수(right) 를 잡고 mid 값을 구해
# for 문을 돌면서 t 값보다 크면 카운팅 해 카운팅이 k 급이 되면 break
# break 되면 건너는 사람이 많다는 소리니까 최고값을 mid 값으로 갱신하고
# 아니다 끝까지 돌았다 그러면 최소값을 mid 값으로 갱신하고 돌려야지
# 그렇게 몇번 계속 돌리다 보면 left 가 right 보다 커질때가 올꺼야 그때 left 값을 출력하면 됨

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    res = 3
    ans = solution(stones, k)
    print(res == ans)