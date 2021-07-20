import sys
N,X = map(int,sys.stdin.readline().split())
N_list = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    if(X>N_list[i]):
        print(N_list[i], end=' ')