# 와 시바 난 DFS 로 막 쪼개서 머리 빠지게 생각하고 있는데
# 그냥 replace 로 해버린다고 이게 말이돼?
# 근데 애초에 DFS 를 한다고 해도 머리 아프게 생각 할것도 아니긴하네
# 어차피 최소로 할려면 무조건 6이 5로 바뀌여야할 것이고
# 최대는 무조건 6으로 바뀌어야겠지
# 괜히 어쩔땐 5고 어쩔땐 6이고 해서 경우의 수를 나눌 할 이유가 없자나
# 무조건 가짓수를 내려야겠다 라고 ㅄ 같이 생각한 내가 존나 문제임


A, B = input().split() #str로 입력

min_num = int(A.replace('6', '5')) + int(B.replace('6', '5')) #replace함수
max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_num, max_num)

# import sys
#
# def DFS(al, aNum, bl, bNum, numSum):
#     global minSum, maxSum
#     if al == aLen and bl == bLen:
#         maxSum = max(maxSum, numSum)
#         minSum = min(minSum, numSum)
#     else:
#         al = al + 1 if al + 1 <= aLen else al
#         bl = bl + 1 if bl + 1 <= bLen else bl
#         if aNum == 5 or aNum == 6:
#
#
#
#
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     a, b = map(int, input().split())
#     aLen, bLen = len(a), len(b)
#     minSum = int(1e9)
#     maxSum = 0
#     DFS(0, a[aLen - 1 - 0], 0, b[aLen - 1 - 0])