# 이분검색
# 임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수
# 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
# 프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.
# ▣ 입력설명
# 첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다.
# 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
# ▣ 출력설명
# 첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
# ▣ 입력예제 1
# 8 32
# 23 87 65 12 57 32 99 81
# ▣ 출력예제 1
# 3

# 여기서 잠깐
# 이분검색이란?
# 검색할 범위를 반으로 줄여가며 찾아가는 검색 이라 한다~

def binarySearch(n, m, arr):
    arr.sort()
    for t in range(1, 3):
        for i in range(n // 2):
            if t == 1:
                if arr[i] == m:
                    return (i + 1)
            else:
                if arr[i + n//2] == m:
                    return (i+1 + n//2)
    return n

def solution(n,m,arr):
    arr.sort()
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] == m:
            return mid + 1
        elif arr[mid] > m:
            rt = mid - 1
        else :
            lt = mid + 1

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

ans = solution(N, M, num_list)

print(ans)
