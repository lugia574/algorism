import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        a, b, c = map(int, input().split())
        if a + b + c == 0: break
        sumNum = a + b + c
        maxNum = max(a, b, c)
        if sumNum - maxNum <= maxNum:
            print("Invalid")
            continue

        nums = set()
        nums.add(a)
        nums.add(b)
        nums.add(c)

        cnt = len(nums)
        if cnt == 3:
            print("Scalene")
        elif cnt == 2:
            print("Isosceles")
        else:
            print("Equilateral")