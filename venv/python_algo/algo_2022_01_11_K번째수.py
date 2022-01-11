# K번째 수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
# 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
# 두 번째 줄에 N개의 숫자가 차례로 주어진다.
# ▣ 출력설명
# 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
# ▣ 입력예제 1
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# ▣ 출력예제 1
# #1 7
# #2 6
# 입력예제1 해설 :
# case 1 : 2 7 3 8의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 7이다.
# case 2 : 8 16 6 6 17 3 10 11의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 6이다

T = int(input())

def K_number(s, e, k, num_list):
    #num_list[s-1] ~ num_list[e-1]
    for i in range(s-1, e):
        for j in range(i, e):
            if num_list[i] > num_list[j]:
                tmp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = tmp
    #print(num_list)
    ans = num_list[s+k-2]
    return ans

for tr in range(1, T+1):
    n, s, e, k = map(int,input().split())
    num_list = list(map(int,input().split()))

    ans=K_number(n,s,e,k,num_list)

    print('#',end="")
    print(tr, ans)
    print()


#################################################

def sol_K_number(s, e, k, num_list):

    num_list = num_list[s-1:e]
    num_list.sort()
    ans = num_list[k-1]

    return ans

# 나는 s~e번째 숫자들 정열을 하고 원래 있는 리스트에서 K번째 수를 찾으라는 건줄 알고
# 슬라이싱 안하고 그 안에서 정렬을 함
# 근데 그냥 s번째에서 e 번째까지의 k 번째 수라
# 그냥 슬라이싱 해서 sort 하면 됐다

# 처음 잘못 안 문제로 푼다고 했을떄
# s~e 번째까지 슬라이싱 하고 sort 한 다음
# 해당 index에 sort한 s~e 번째를 다시 박아서 list[k-1] 했음 더 깔끔하게 됐을 것이다.