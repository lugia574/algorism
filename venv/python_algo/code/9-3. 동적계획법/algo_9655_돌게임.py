# 상근이가 먼저 그담에 창영
# 돌은 1, 3 개 홀수임
# 그냥 어떻게 하든 n%2 했을때 나머지가 있으면 상근이가 이기는거 아님?
# 그냥 홀수로밖에 못가져가면 어떻게 가져가든 창영이때부터 짝수가 되는데
# 그럼 그냥 나머지 수가 홀수면 그만큼 상근이가 더 가져가는거자너

# 가령 8개라고 했을때 33/ 1 1 창영 이김 11/ 11/ 11/ 11 창영 이김
# 9개라고 했을때 33/ 3 상근 이김, 33/ 11/ 1 상근 이김,  11/ 11/ 11/ 11/ 1 상근 이김
# 더 증명 필요한가?
# 다이나믹 프로그래밍이 아닌거 같은데
# 어떻게 보면 맞긴한데 흠흠흠
import sys

if __name__ == "__main__":
    print("SK" if int(sys.stdin.readline())%2 != 0 else "CY")
    # 돌게임 2 코드
    # print("SK" if int(sys.stdin.readline())%2 == 0 else "CY")