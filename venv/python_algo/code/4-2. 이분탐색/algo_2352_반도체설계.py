# 이거 내가 dp 로 풀었던 문제 아님?
# 다리짓는 문제?
# 그때 dp 2중 포문 갈겼는데 그러면 터지겠는데 n 값이 4만임 무조건 터짐
# 우선 보면 이 문제는 전형적인 최장 증가 부분 수열이랑 같음 
# 왜냐 기본적으로 현재 값보다 무조건 다음 값이 더 커야 하기 때문임
# 그렇다면 당연하게 증가하는 부분 수열이 되는거고 그중에서 가장 긴 길이가 되는 부분 수열이 찾으라는 소리가 됨
# 이 문제의 테케의 경우 4 2 6 3 1 5 배열에서 2 3 5 순으로 증가해야지 3자리로 가장 긴 배열이 된다는 거임
# 여기서 dp 방식을 쓰면 시초가 될테니 이분탐색을 이용해서 풀꺼임
# 첫 인덱스 값은 res 배열에 넣고 이후 반복문을 돌려
# 배열 맨 윗 값이 < 반복문 i 이면 그대로 res 배열에 박아 넣고
# 아니다 반복문 i 값이 더 작다 이러면 이제 binary 를 돌려서 res 어디에 들어가야하나 정해
# 업, 다운 하면서 위치를 특정하고 거기 값으로 값을 res 갱신해줘
# 그렇게 계속 굴리면 갯수가 나옴
# 근데 이게 문제가 뭐냐면 갯수는 맞게되는데 깊게 들어가면 이게 2, 1, 5 가 되거든? 이럼 틀린 답이야
# 이게 참 먼가 이해가 안가 어떻게 조건이 안맞게 구현을 했는데 갯수는 맞게 되는거지?
# 어차피 res -1 을 경우를 제외하곤 어떻게 되든 상관없어서 그런가?
# 막말로 res = [0 0 0 0 5] 상태라고 해도 잘 돌아가긴 해 res[-1] 부분은 멀쩡하니까
# 이건 나중에 다시 한번 봐야할듯 솔까 이해가 잘 안됨

import sys

def binary(target):
    start = 0
    end = len(res) - 1

    while start <= end:
        mid = (start + end) // 2

        if res[mid] == target:
            return mid
        elif res[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    res = [arr[0]]
    for i in range(1, n):
        if res[-1] < arr[i]:
            res.append(arr[i])
        else:
            index = binary(arr[i])
            res[index] = arr[i]

    print(len(res))
    print(res)

    # 13
    # 4 2 6 3 1 7 0 0 0 0 4 5 6

    # 이부분은 이제 갯수를 구하라는게 아니라 올바른 배열을 뱉어라 라고 했을때 구현된 코드임 (gpt 한태 물어봄)
    # def longest_increasing_subsequence(arr):
    #     lis = []  # 가장 긴 증가하는 부분 수열을 저장하는 배열
    #     parents = [-1] * len(arr)  # 이전 요소의 인덱스를 저장하는 배열
    #
    #     for i in range(len(arr)):
    #         num = arr[i]
    #         if not lis or lis[-1][0] < num:
    #             if lis:
    #                 parents[i] = lis[-1][1]
    #             lis.append((num, i))
    #         else:
    #             # 이분 탐색을 통해 적절한 위치를 찾아서 대체
    #             left, right = 0, len(lis) - 1
    #             while left <= right:
    #                 mid = (left + right) // 2
    #                 if lis[mid][0] >= num:
    #                     right = mid - 1
    #                 else:
    #                     left = mid + 1
    #             if left > 0:
    #                 parents[i] = lis[left - 1][1]
    #             lis[left] = (num, i)
    #
    #     idx = lis[-1][1]
    #     result = []
    #     while idx != -1:
    #         result.append(arr[idx])
    #         idx = parents[idx]
    #
    #     return result[::-1]  # 역순으로 출력을 위해 뒤집은 배열 반환
    #
    # n = int(input())
    # arr = list(map(int, input().split()))
    #
    # result = longest_increasing_subsequence(arr)
    # print(*result)