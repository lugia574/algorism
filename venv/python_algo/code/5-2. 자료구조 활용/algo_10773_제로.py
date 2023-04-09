import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    nums = []
    for _ in range(t):
        num = int(input())
        if num == 0:
            nums.pop()
        else:
            nums.append(num)
    print(sum(nums))