import sys
from itertools import combinations

if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        numArr = list(map(int,input().rstrip().rsplit()))
        if numArr[0] == 0:
            break
        del numArr[0]
        numArr.sort()
        ans = list(combinations(numArr, 6))

        for x in ans:
            for i in x:
                print(i, end=" ")
            print()
        print()
