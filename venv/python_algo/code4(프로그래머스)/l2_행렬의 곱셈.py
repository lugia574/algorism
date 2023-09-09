# https://velog.io/@falling_star3/프로그래머스-Level2-행렬의-곱셈

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


if __name__ == "__main__":
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [3, 3]]
    res = [[15, 15], [15, 15], [15, 15]]

    answer = solution(arr1, arr2)
    print(res == answer)

    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    res = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

    answer = solution(arr1, arr2)
    print(res == answer)