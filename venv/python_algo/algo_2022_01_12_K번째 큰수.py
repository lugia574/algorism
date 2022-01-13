# K번째 큰 수
# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가
# 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
# 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
# 하는 프로그램을 작성하세요.
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
# 은 22입니다.
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력
# 된다.
# ▣ 출력설명
# 첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
# ▣ 입력예제 1
# 10 3
# 13 15 34 23 45 65 33 11 26 42
# ▣ 출력예제 1
# 143

def Kmax(n,n_list,k):
    list_sum = []
    for x in range(n):
        for y in range(x+1,n):
            for z in range(y+1,n):
                sum_num = n_list[x] + n_list[y] + n_list[z]
                if sum_num not in list_sum:
                    list_sum.append(sum_num)
    list_sum.sort(reverse=True)
    # print('이건 내가 한거',list_sum)
    return list_sum[k-1]




# 띠요용 
#################################


def sol_kmax(n,num_list,k):
    res = set()

    for i in range(n):
        for j in range(i+1, n):
            for m in range(j+1,n):
                res.add(num_list[i] + num_list[j]+ num_list[m])
    res = list(res)
    res.sort(reverse=True)
    # print('선생이 한거',res)
    ans = res[k-1]
    return ans


n, k = map(int,input().split())
num_list = list(map(int,input().split()))

ans = sol_kmax(n,num_list,k)
Kmax(n,num_list,k)

print(ans)

## 실수 1. 글을 제대로 안읽음 K 번째 큰수면 내림차순으로 sort 해서 위에서부터 K번째 수를 찾아야지 무슨 올림차순으로 함?
## 실수 2. 중복 제거를 안함 그냥 중복도 치는 줄 알았음 >> 글을 제대로 안읽었다