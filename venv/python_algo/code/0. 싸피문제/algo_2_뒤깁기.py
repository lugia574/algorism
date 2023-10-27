# 뒤집기
# 주어진 수열의 일부를 골라서 수열을 뒤집어 읽어도
# 동일한 수열이 되는 가장 긴 경우를 찾아서 그 수열의 길이를 구하시오
# 단, 수열을 고를 때 연속적일 필요는 없으나 순서는 유지 되어야 한다.

# 예제 입력)
# 3, 2, 8, 1, 4, 1, 6, 8, 3, 4, 5, 6, 4, 3

# 예제 결과)
# 7

# 풀이)
# 3, 4, 6, 8, 6, 4, 3 이렇게 해서 가장 수열이 된다

# 흐음 약간 부분 수열 문제 아닌가???
# 문제는 쭈욱 높은 순으로 하는게 아니라 각 idx 에 맞는 값이라는거지
# 그냥 2중 배열 조지는게 더 직관적으로 나을수도??

def solution(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    max_len = 0

    for i in range(n):
        dp[i][i] = 1
        max_len = max(max_len, 1)

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                if j - i == 1:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

            max_len = max(max_len, dp[i][j])

    return max_len

if __name__ == "__main__":
    arr = [3, 2, 8, 1, 4, 1, 6, 8, 3, 4, 5, 6, 4, 3]
    res = 7
    answer = solution(arr)
    print(res == answer, answer)

    arr = [7, 5, 8, 7, 8, 5, 8, 1, 4, 8]
    answer = solution(arr)
    print(answer)

    arr = [8, 6, 5, 5, 5, 3, 3, 5, 7, 3, 6, 10, 8, 5, 5]
    answer = solution(arr)
    print(answer)

    arr = [4, 19, 13, 19, 4, 12, 13, 14, 12, 4, 8, 2, 13, 13, 12, 13, 4, 14, 8, 8]
    answer = solution(arr)
    print(answer)

    arr = [20, 13, 13, 21, 13, 34, 17, 11, 13, 21, 11, 20, 13, 40, 20, 20, 32, 34, 32, 13, 22, 21, 12, 34, 21, 34, 21, 17]
    answer = solution(arr)
    print(answer)