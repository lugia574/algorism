def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        tmp = a % b
        a = b
        b = tmp

    return a


def solution(arr):
    length = len(arr)
    if length == 1:
        return arr[0]

    g = gcd(arr[0], arr[1])
    answer = arr[0] * arr[1] // g

    if length > 2:
        for i in range(2, length):
            g = gcd(answer, arr[i])
            answer = answer * arr[i] // g

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline