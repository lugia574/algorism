# 조용한데 찾기
#
# 2
# 20 10 10
# 3
# 25 10
# 20 15
# 70 70
# 50 50 100
# 4
# 0 0
# 0 100
# 100 0
# 100 0


# 받기
T = int(input())

for t in range(T):

    a,b,r = map(int,input().split())
    N = int(input())

    x = [0 for _ in range(N)]

    for i in range(N):
        x[i]=list(map(int, input().split()))

    def sol (a,b,r,N,x):
        for i in range(N):
            d = ((x[i][0] - a) ** 2) + ((x[i][1] - b) ** 2)

            if d >= r **2:
                print('silent')

            else:
                print('nosiy')


    sol(a,b,r,N,x)

