#00이 입력될때까지 계속 받고 그것들을 출력할것

while True:
    A,B = map(int, input().split())
    if A==0 and B==0:
        break

    print(A+B)

