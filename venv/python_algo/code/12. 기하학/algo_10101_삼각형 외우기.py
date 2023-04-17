import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    degree = [int(input()) for _ in range(3)]
    degreeSum = sum(degree)

    if degree[0] == 60 and degree[1] == 60 and degree[2] == 60:
        print("Equilateral")
    elif degreeSum == 180:
        if degree[0] != degree[1] and degree[0] != degree[2] and degree[1] != degree[2]:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Error")
