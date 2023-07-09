# 2, 3, -6, 1, 3, -1, 2, 4
# 2 3 9 10 3 4 6 4
# 나는 말이다 어차피 -1 1 -1 ~~ or 1 -1 1 -1 ~~ 두개 적용하느니
# 그냥 본인 index 기준 와리가리가 얼마나 되는지 그리고 그 와리가리 되는 값만의 합이 얼마나 되는지가 핵심이라고 봤거든?
# 이게 -2 2 -2 2 이렇다고 했을때 -1, 1, -1, 1 을 곱해주면 되자너
# 근데 말이야 와리가리가 되냐 안되냐를 판단할게 아니라
#  [-999, -1, 2, 999] * [-1, 1, -1, 1] = [999, -1, -2, 999] 가 되는데  이땐 와리가리가 안된다 해도 존나 높을꺼 아녀
# 그니까 그냥 와리가리 기준으로 DP 를 할게 아니고 누적합 같은걸 해야지 않나

# https://velog.io/@jaehyeonkim2358/프로그래머스Python-연속-펄스-부분-수열의-합
import sys


def solution(sequence):
    answer = -sys.maxsize
    size = len(sequence)
    s1 = s2 = 0  # 1
    s1_min = s2_min = 0  # 2
    pulse = 1

    for i in range(size):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)

        # 3
        answer = max(answer, s1 - s1_min, s2 - s2_min)

        # 4
        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)

        # 5
        pulse *= -1
    return answer

if __name__ == "__main__":
    sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    result = 10

    answer = solution(sequence)
    print(answer == result, answer)