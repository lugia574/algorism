def solution(N,M, k):

    if k== M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
    if k == 0 :
        for i in range(1, N+1):
            if nums[i] != 1:
                arr.append(i)
                nums[i] = 1
                solution(N,M,k+1)
                nums[i] = 0
                arr.remove(i)
    else:
        for i in range(1, N+1):
            if nums[i] != 1:
                if i > arr[k-1]:
                    arr.append(i)
                    nums[i] = 1
                    solution(N,M,k+1)
                    nums[i] = 0
                    arr.remove(i)

N, M = map(int,input().split())

arr = []
nums = [0] * 10

solution(N, M, 0)
