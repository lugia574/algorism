import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    mArr = list(map(int, input().split()))

    arr.sort()

    for num in mArr:
        lt, rt = 0, n - 1
        isExist = False

        while lt <= rt:
            mid = (lt + rt) // 2
            if num == arr[mid]:
                isExist = True
                print(1)
                break
            elif num > arr[mid]:
                lt = mid + 1
            else:
                rt = mid - 1

        if not isExist:
            print(0)