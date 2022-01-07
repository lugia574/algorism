def solution(N,M, k):

    if k== M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return

    if k == 0:
        for i in range(1, N+1):
            arr.append(i)
            solution(N,M,k+1)
            del arr[k]
    else:
        for i in range(1, N+1):
            if i >= arr[k-1]:
                arr.append(i)
                solution(N,M,k+1)
                del arr[k]

N, M = map(int,input().split())

arr = []

solution(N, M, 0)
