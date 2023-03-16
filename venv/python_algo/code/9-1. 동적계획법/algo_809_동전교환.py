# 동전교환
# 다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환
# 해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.
# ▣ 입력설명
# 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종
# 류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
# 각 동전의 종류는 100원을 넘지 않는다.
# ▣ 출력설명
# 첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
# ▣ 입력예제 1
# 3
# 1 2 5
# 15
# ▣ 출력예제 1
# 3
# 설명 : 5 5 5 동전 3개로 거슬러 줄 수 있다.

# 전에 풀었던거다
# 전에는 재귀 써서 각각 3진 트리로 뻗어 나가서 가장 작은 counter 로 계속 갱신해주고 그 값을 출력 했음
# 세고 있는 counter가 저장했던 counter 보다 높아지면 바로 컷 해서 가지치기함

def fnc():
    for coin in coinArr:
        for j in range(1,m+1):
            check[j] = min(check[j], check[j-coin] + 1)

def inputFnc():
    n = int(input())
    coinArr = list(map(int,input().split()))
    m = int(input())
    return  n, coinArr, m

if __name__ == "__main__":
    n, coinArr, m = inputFnc()
    check = [999] * (m+1)
    check[0] = 0
    fnc()
    print(check[m])