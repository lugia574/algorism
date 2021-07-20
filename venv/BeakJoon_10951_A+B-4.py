# 이건 예외 처리 문제임

# while True:
#     try:
#         A,B = map(int, input().split())
#         print(A + B)
#     except:
#         break


try:
    while True:
        A, B = map(int, input().split())
        print(A + B)
except:
    pass