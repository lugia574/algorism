# 아파트 입주자 구하기
#(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# K 층에 N 호에는 몇명이 살고 있는가
#단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 1 ≤ k, n ≤ 14

def ap_cnt (K, N):
    apt = [[0 for _ in range(15)] for _ in range(15)]

    for i in range(15):
        apt[i][1] = 1
        apt[0][i] = i

    for i in range(1, 15):
        for j in range(2, 15):
            apt[i][j] = apt[i][j - 1] + apt[i - 1][j];

    return apt[K][N]


T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())

    print(ap_cnt(K,N))