# 딕셔너리 정렬 하는 문제
# https://yuna0125.tistory.com/83
# 처음에 값을 cnt 해줄땐 딕셔너리로 막 해줬지
# 근데 이걸 정렬할려면 결국 리스트로 만들어야함
# sorted 는 리스트로 반환해주니까 저렇게 리스트 안에 튜플 형태로 반환을 해줌
# 그걸 이제 다시 재정렬 하면서 key 로 조건을 주고, reverse=True 로 역순으로 딱 해준거임

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
    
    print(books, type(books))
    
    books = sorted(books.items())
    print(books, type(books))
    
    books = sorted(books, key = lambda x : x[1], reverse = True)
    print(books, type(books))
    
    print(books[0][0])