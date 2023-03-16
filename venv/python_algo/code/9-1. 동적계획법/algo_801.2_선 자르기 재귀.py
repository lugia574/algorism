# 재귀, 메모이제이션
# ▣ 입력설명
# 첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.
# ▣ 입력예제 1
# 7
# ▣ 출력예제 1
# 21

# 801 해당 점화식을 재귀로 함 구현 해보자

def DFSFn(n):
    if dy[n] != 0:
        return dy[n]
    else:
        dy[n] = DFSFn(n - 1) + DFSFn(n - 2)
        return dy[n]

if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)
    dy[1] = 1
    dy[2] = 2
    res = DFSFn(n)
    print(res)
