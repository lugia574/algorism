# https://sungmin-joo.tistory.com/67
# 사실상 String 문제라고 봐야하는거 아닌가
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = input().split('-')
    s = 0
    for i in arr[0].split('+'):
        s += int(i)
    for i in arr[1:]:
        for j in i.split('+'):
            s -= int(j)
    print(s)