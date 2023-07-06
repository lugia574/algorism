# 딕셔너리 정렬 하는 문제
# https://yuna0125.tistory.com/83

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    books = {}
    for _ in range(n):
        b = input().strip()
        if b not in books:
            books[b] = 1
        else:
            books[b] += 1

    books = sorted(books.items())
    books = sorted(books, key = lambda x : x[1], reverse = True)
    print(books[0][0])